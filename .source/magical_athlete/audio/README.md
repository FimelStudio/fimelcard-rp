# 胡闹运动会音频

`bgm.wav` 是 Fimel Card 原创轻快运动主题：C 大调、120 BPM、4/4 拍、16 小节，共 32 秒（640 游戏刻）。旋律、低音、拨弦和打击乐均由生成器合成，无第三方采样。其余短音效也为原创合成，许可 CC0-1.0。

掷骰事件复用已经合并的 [Kenney Casino Audio 1.1](https://kenney.nl/assets/casino-audio) `dice-throw-1.ogg`，许可为 CC0；原始文件及许可在 `.source/catan/audio/kenney/casino/`。运行资源引用同一 Ogg，不重复打包。

独立事件为 `magical_athlete:roll/step/land/skill/trip/warp/coin/finish/race_start/win/illegal/bgm`。音乐流式加载，建议播放音量 0.16，可在本桌设置关闭；暂停、结束、离桌和旧局重连时停止对应事件。所有播放仅发送本桌玩家。

重建：在数据包根目录运行 `python tools/build_magical_athlete_sound.py`，需要 NumPy、ffmpeg。原始无损 WAV、乐曲说明、许可及每个输出的 SHA-256 均保留在本目录。音乐首尾使用短淡化消除点击，播放循环不改变规则或骰值。

## 狂野赛道音乐

`bgm_wild.ogg` 为用户提供的《wake up》，原始文件保留在 `imports/wake up.ogg`。普通赛道仍使用原创 `bgm`。两首均按 0.16 播放；新增曲目先转单声道，再以两遍响度归一化与瞬时峰值限制对齐普通曲目的综合响度，保留完整时长，按实际长度循环。响度、时长与哈希见 manifest。

此曲不属于本目录原创合成音频的 CC0 授权；未提供额外许可信息。重建时运行 `python tools/build_magical_athlete_music.py`，无需再次访问原始磁盘路径。切换赛道会先停止旧曲，暂停、关闭音乐、结束游戏及离桌均停止两种音乐。
