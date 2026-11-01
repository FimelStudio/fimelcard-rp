# 围棋原创音效

共八段落子、提子、收回与短促提示，由 Fimel Cards 数学合成，不使用商业游戏录音，不新增前置。
44,100 Hz、单声道、16 bit PCM 源文件保留在此；发布用 Vorbis OGG 在 assets/card/sounds/weiqi/。
脚本 tools/build_weiqi_sound.py，固定随机种子 20261101，需要 NumPy 与 FFmpeg。
audio_manifest.json 保存时长和发布文件 SHA-256；sound 回调限定本桌玩家，使用 Minecraft 方块音量分类。
