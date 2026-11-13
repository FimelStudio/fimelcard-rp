"""校验象棋原音效哈希、Ogg格式与转码波形；需FFmpeg和NumPy。"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import numpy as np


SOURCE = Path(__file__).resolve().parent
CARD = SOURCE.parents[1] / 'assets/card'


def main():
    ffmpeg = shutil.which('ffmpeg')
    assert ffmpeg, 'FFmpeg is required'
    ffprobe = Path(ffmpeg).with_name('ffprobe.exe')
    manifest = json.loads((SOURCE/'sounds/source_manifest.json').read_text(encoding='utf-8'))
    results = []
    def decode(path):
        raw = subprocess.check_output([ffmpeg, '-v', 'error', '-i', str(path), '-ac', '1', '-ar', '44100', '-f', 'f32le', '-'])
        return np.frombuffer(raw, dtype='<f4')
    for record in manifest['sources']:
        original = SOURCE/'sounds'/record['file']
        assert hashlib.sha256(original.read_bytes()).hexdigest() == record['sha256'], original
        name = 'gong' if original.stem == 'gong-game-start-end' else original.stem
        output = CARD/'sounds/xiangqi'/(name+'.ogg')
        info = json.loads(subprocess.check_output([str(ffprobe), '-v', 'error', '-show_streams', '-of', 'json', str(output)], text=True))['streams']
        assert len(info) == 1 and info[0]['codec_name'] == 'vorbis' and info[0]['channels'] == 1 and info[0]['sample_rate'] == '44100', info
        before, after = decode(original), decode(output)
        assert np.isfinite(after).all() and np.max(np.abs(after)) > .01
        assert abs(len(before)-len(after)) <= 2048, (original, len(before), len(after))
        length = min(len(before), len(after))
        correlation = float(np.corrcoef(before[:length], after[:length])[0, 1])
        assert correlation > .97, (original, correlation)
        results.append({'file': output.name, 'seconds': round(len(after)/44100, 3), 'correlation': round(correlation, 6), 'bytes': output.stat().st_size})
    events = json.loads((CARD/'sounds.json').read_text(encoding='utf-8'))
    for event in ('move', 'capture', 'check', 'start', 'end', 'illegal'):
        entry = events['xiangqi.'+event]
        for language in ('zh_cn', 'en_us'):
            assert entry['subtitle'] in json.loads((CARD/'lang'/(language+'.json')).read_text(encoding='utf-8'))
        for sound in entry['sounds']:
            if sound.get('type') != 'event':
                assert sound['name'].startswith('card:') and (CARD/'sounds'/(sound['name'].split(':')[1]+'.ogg')).is_file()
    print(json.dumps({'sources': results, 'events': 6, 'status': 'PASS'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
