"""将 Chess.com default 原始音效转换成 Minecraft 使用的单声道 Vorbis。

运行：python .source/chess/export_sounds.py，需要 FFmpeg。
原文件、下载地址和 SHA-256 保存在 sounds/ 中；重建时无需联网。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


SOURCE = Path(__file__).resolve().parent
CARD = SOURCE.parents[1] / "assets/card"
NAMES = ["move", "capture", "castle", "check", "start", "end", "illegal"]


def merge(path, additions):
    content = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    content.update(additions)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ffmpeg", default=shutil.which("ffmpeg"))
    args = parser.parse_args()
    if not args.ffmpeg:
        parser.error("请将 FFmpeg 加入 PATH，或用 --ffmpeg 指定路径")
    manifest = json.loads((SOURCE / "sounds/source_manifest.json").read_text(encoding="utf-8"))
    records = {entry["event"]: entry for entry in manifest["sources"]}
    # 先验证整套原文件，避免缺失或被改写的来源混入运行资源。
    for name in NAMES:
        entry = records[name]
        source = SOURCE / "sounds/default" / entry["file"]
        if hashlib.sha256(source.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("原始音效校验失败：" + str(source))
    output = CARD / "sounds/chess"
    output.mkdir(parents=True, exist_ok=True)
    stats = []
    for name in NAMES:
        entry = records[name]
        source = SOURCE / "sounds/default" / entry["file"]
        dest = output / (name + ".ogg")
        # 只转换声道、采样率和编码，保持原声音色、节奏、音高与响度。
        subprocess.run([str(args.ffmpeg), "-hide_banner", "-loglevel", "error",
                        "-y", "-i", str(source), "-map_metadata", "-1",
                        "-ac", "1", "-ar", "44100", "-fflags", "+bitexact",
                        "-flags:a", "+bitexact", "-c:a", "libvorbis", "-q:a", "6",
                        str(dest)], check=True)
        stats.append({"event": name, "source": entry["file"], "bytes": dest.stat().st_size})
    merge(CARD / "sounds.json", {
        "chess." + name: {
            "subtitle": "subtitles.card.chess." + name,
            "sounds": [{"name": "card:chess/" + name, "attenuation_distance": 12}],
        } for name in NAMES
    })
    translations = {
        "zh_cn": ["棋子落下", "棋子被吃", "王车易位", "将军", "棋局开始", "棋局结束", "走法不合法"],
        "en_us": ["Piece moves", "Piece captured", "Castling", "Check", "Game starts", "Game ends", "Illegal move"],
    }
    for language, labels in translations.items():
        merge(CARD / "lang" / (language + ".json"), {
            "subtitles.card.chess." + name: label for name, label in zip(NAMES, labels)
        })
    print(json.dumps({"provider": manifest["provider"], "theme": manifest["theme"],
                      "sounds": stats, "format": "mono 44100 Hz Ogg Vorbis"}, indent=2))


if __name__ == "__main__":
    main()
