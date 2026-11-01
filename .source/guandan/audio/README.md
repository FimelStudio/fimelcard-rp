# 掼蛋原创音效

共九段扑克纸张声、桌面点击和短促提示，由 Fimel Cards 数学合成，不使用商业游戏录音，不新增前置。
44,100 Hz、单声道、16 bit PCM 源文件保留在此；发布用 Vorbis OGG 在 assets/card/sounds/guandan/。
脚本 tools/build_guandan_sound.py，固定随机种子 20261101，需要 NumPy 与 FFmpeg。
audio_manifest.json 保存时长和发布文件 SHA-256；sound 回调限定本桌玩家，使用 Minecraft 方块音量分类。
