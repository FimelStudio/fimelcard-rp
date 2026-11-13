# 璀璨宝石音频来源

沿用数据包已合并的 CC0 声音，不重复打包音频：

- 拿取／退回宝石：Kenney《Casino Audio 1.1》chips-collide-1.ogg。
- 预约牌：同包 card-shove-1.ogg。
- 购买开发牌：Kenney《Impact Sounds 1.0》impactWood_medium_000.ogg。
- 贵族到访／胜利：同包 impactBell_heavy_000.ogg。
- 无法操作：同包 impactSoft_medium_000.ogg。
- 可关闭背景音乐：RandomMind《Medieval: The Old Tower Inn (loop)》。

来源：[Casino Audio](https://kenney.nl/assets/casino-audio)、[Impact Sounds](https://kenney.nl/assets/impact-sounds)、[The Old Tower Inn](https://opengameart.org/content/medieval-the-old-tower-inn)。
均为 CC0-1.0；作者原文件、页面快照、许可和编码记录保存在 ../../catan/audio/（从资源包 .source 根目录定位为 catan/audio/）。
本目录 manifest.json 逐项记录实际引用、原始文件、处理参数和 SHA-256。事件独立注册在 assets/splendor/sounds.json，引用 assets/card/sounds/catan/，不改其他游戏声音。
在数据包根目录运行 python tools/build_splendor_sound.py 重建事件注册和播放函数；需要重新编码公共音源时使用 python tools/build_catan_sound.py --assets（需 ffmpeg）。

音乐仅发送本桌玩家，使用独立 splendor:bgm 事件；关闭选项、暂停、结束、清理和旧局重连都应调用 stop／stop_player。恢复对局可重新从曲首播放，不改变规则状态。
