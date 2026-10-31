# 五子棋与飞行棋音效

全部由 Fimel Cards 自行合成，无外部音频或运行时前置。
无损源位于 audio/，发布资源为 assets/card/sounds/ 中的单声道 Vorbis OGG。
五子棋使用短促木石敲击；飞行棋使用逐渐放慢的骰子撞击、逐格轻敲、起飞与飞越风声、撞机和到达音。
从数据包根目录运行 `python tools/build_boardgame_sound.py`，依赖 NumPy 与 FFmpeg。
随机种子20261031、采样率44100 Hz，参数在生成脚本中；manifest.json记录时长及输出SHA-256。
声音由本桌控制器定位，发送给仍属于本桌的玩家，音量受Minecraft「方块」分类控制。
