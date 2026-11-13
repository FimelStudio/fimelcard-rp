# 卡坦岛音频来源

本目录保留实际使用的原始音频、作者声明页面快照、CC0 许可和 SHA-256 清单。所有音频均允许修改、再分发和商业使用，不依赖网页播放器、视频网站提取或未知来源的录音。

| 用途 | 作品与作者 | 原始许可 |
| --- | --- | --- |
| 投骰、交易、强盗、开发牌 | [Casino Audio 1.1 — Kenney](https://kenney.nl/assets/casino-audio) | CC0；原包 `kenney/casino/License.txt` |
| 建路、建村、城市、胜负与无效操作 | [Impact Sounds 1.0 — Kenney](https://kenney.nl/assets/impact-sounds) | CC0；原包 `kenney/impact/License.txt` |
| 田园／中世纪背景音乐 | [Medieval: The Old Tower Inn — RandomMind](https://opengameart.org/content/medieval-the-old-tower-inn) | 作者发布页明确为 CC0；使用作者提供的循环 WAV |

原作者署名虽非 CC0 强制条件，仍在此保留，感谢 Kenney 与 RandomMind。CC0 完整文本见 `CC0-1.0.txt`，在线版本为 <https://creativecommons.org/publicdomain/zero/1.0/>。

`downloads.json` 记录原始地址、下载包摘要与下载日期；`manifest.json` 记录保留文件和生成 OGG 的 SHA-256、过滤器、编解码器与时长。Kenney 原包仅摘取所用素材，不保留未使用的素材。作者页面快照用于保留许可声明，里面的示例图片和网页装饰资源未加入游戏。

在数据包仓库执行 `python tools/build_catan_sound.py --assets` 可使用本目录原文件重新编码并合并专属音效／字幕键。需要 FFmpeg 的 `libvorbis` 和 FFprobe。音效转为单声道 44.1 kHz；背景音乐保留作者原循环长度，柔和降音量后编码为流式 OGG。没有在首尾加淡入淡出破坏作者的循环点。

音乐属于 Minecraft 的「唱片机／音符盒」音量分类，可在大厅或对局菜单关闭。仅同桌参与者收到播放指令；结束、重载或离座会停止本游戏的背景音乐。
