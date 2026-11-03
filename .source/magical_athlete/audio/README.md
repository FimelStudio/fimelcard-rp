# 胡闹运动会音频

`bgm.wav` 是 Fimel Cards 原创轻快运动主题：C 大调、120 BPM、4/4 拍、16 小节，共 32 秒（640 游戏刻）。旋律、低音、拨弦和打击乐均由生成器合成，无第三方采样。其余短音效也为原创合成，许可 CC0-1.0。

掷骰事件复用已经合并的 [Kenney Casino Audio 1.1](https://kenney.nl/assets/casino-audio) `dice-throw-1.ogg`，许可为 CC0；原始文件及许可在 `.source/catan/audio/kenney/casino/`。运行资源引用同一 Ogg，不重复打包。

独立事件为 `magical_athlete:roll/step/land/skill/trip/warp/coin/finish/race_start/win/illegal/bgm`。音乐流式加载，建议播放音量 0.16，可在本桌设置关闭；暂停、结束、离桌和旧局重连时停止对应事件。所有播放仅发送本桌玩家。

重建：在数据包根目录运行 `python tools/build_magical_athlete_sound.py`，需要 NumPy、ffmpeg。原始无损 WAV、乐曲说明、许可及每个输出的 SHA-256 均保留在本目录。音乐首尾使用短淡化消除点击，播放循环不改变规则或骰值。
