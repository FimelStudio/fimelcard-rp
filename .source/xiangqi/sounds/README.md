# 中国象棋音效来源

落子、吃子和开局／结束锣声来自 [Xiangqi.com 的音效下载页](https://www.xiangqi.com/help/sounds)。该页提供整套声音下载供使用；原始下载包为 `https://www.xiangqi.com/s/xq-sounds.zip`。

这里只保存使用到的三个原始 MP3，下载地址、下载时间和 SHA-256 见 `source_manifest.json`。声音来源归 Xiangqi.com。将军和非法走法提示分别引用 Minecraft 原版音符盒铃声和低音。

从资源包目录运行 `python .source/xiangqi/export_sounds.py` 重建，需 FFmpeg。脚本校验原文件，转换为单声道 44.1 kHz Vorbis，保留原音色。只合并 `card:xiangqi.*` 事件及字幕，不覆盖其他游戏。

运行 `python .source/xiangqi/check_sounds.py` 可检查原文件哈希、Vorbis 格式、字幕及转码波形，另需 NumPy；三段转码与原音频的相关系数均高于 0.997。
