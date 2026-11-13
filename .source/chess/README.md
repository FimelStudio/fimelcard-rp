# 国际象棋资源与来源

棋子几何来自 **16bit 制作组的 NyaaWorks 喵工坊 r2.2**，源目录为
`assets/minecraft/models/item/nw/chess`。本项目内置白／黑各六种棋子的模型，
原始几何副本保存在 `nyaaworks/`，来源和 SHA-256 见 `source_manifest.json`。
上游作者：[16bit 制作组](https://space.bilibili.com/2907002)。使用时请保留相关来源署名。

本项目调整：以 `none` 展示模式适配桌面大小；新增黑檀黑白、胡桃木、冰蓝、
翡翠四组材质，棋盘新增经典黑白、绿白、木棕、蓝灰、紫白五组常见配色。
新增材质、棋盘和坐标均由脚本绘制，未复制第三方网站的棋盘图片。
`board-palettes.png` 为棋盘配色预览，不属于游戏运行资源。

资源命名为 `card:chess/<palette>/<white|black>_<pawn|knight|bishop|rook|queen|king>`；
棋盘为 `card:chess/board_<classic|green|wood|blue|purple>`。

从数据包目录运行 `python tools/build_chess_visual.py` 重建全部棋盘、材质、
模型及桌面展示函数，需要 Pillow。首次运行可从相邻的 NyaaWorks 资源包读取原始模型；
此后只需本目录保存的原始副本，不要求玩家另外安装 NyaaWorks。

坐标：逻辑 a1=0、h8=63；四座格长 0.27、八座 0.37，棋盘内部边长 2.16／2.96。
外围坐标边框各为格长的 3/8。棋盘底面位于桌心 Y+1.02，棋子底面为 Y+1.04。
方向 0 白方从南向北；方向 1 整盘旋转 90 度，白方从西向东。
棋盘的右旋 Y 180 度抵消原版 ItemDisplayRenderer 的固定 Y 180 度，避免贴图与逻辑坐标反向。
从白方看，字母左至右为 a～h，数字近至远为 1～8，王位于 e1／e8；逻辑棋格与交互位置不变。
王在统一展示变换中额外水平旋转 90 度，马额外水平旋转 180 度；四组配色、黑白双方及移动／吃子／重建状态均一致。
选中格使用金色边框；开启走格提示后，全部合法终点以翡翠绿色发光边框显示。
提示复用规则引擎的只读模拟，包含将军、牵制、易位、吃过路兵和升变合法性。
64 个棋格右键区宽度分别为 0.266／0.366、高度 0.025，不遮挡远处空格。
另为每枚棋子生成一个窄命中区，依据原始几何的旋转包围盒与桌型缩放覆盖完整高度；
王、后顶部同样可点。命中区随行棋／易位同步移动，升变调整尺寸，吃子时移除。

吃子显示保留原棋色，缩小后沿吃子者面向棋盘的右侧桌沿两列排列；没有实际玩家座位的
预览使用棋盘默认白／黑方向。两人若坐在同一桌边，共享右侧边槽并缩小为四条队列。
游戏开局会按阵营自动安排到棋盘对应的相对侧，便于阅读坐标。
行棋、王车易位、被吃棋子移至边槽均使用 8 刻展示变换插值。

## 棋局音效

`assets/card/sounds/chess/` 内置移动、吃子、易位、将军、开局、结束和非法走法
七种音效，事件为 `card:chess.<move|capture|castle|check|start|end|illegal>`。
音频使用 [Chess.com 默认音效](https://www.chess.com/forum/view/general/chessboard-sound-files?page=2)，
来源为 `images.chesscomfiles.com/chess-themes/sounds/_MP3_/default/`。
原始 MP3、每个文件的下载地址与 SHA-256 保存在 `sounds/`，来源归 Chess.com。

运行 `python .source/chess/export_sounds.py` 重建音频，需要 Python 和 FFmpeg；
可用 `--ffmpeg <路径>` 指定编码器。脚本先校验本地原文件，只转换声道、采样率和编码，
不合成或修改音色；仅合并 `sounds.json` 的 `chess.*` 事件及中英文字幕。
运行资源为单声道 44.1 kHz Ogg Vorbis，支持棋盘位置的空间声音；重建无需联网。

数据包在 8 刻动画落位时选取一个音效：将军优先，其次易位、吃子、普通移动；
将死等终局播放结束音。非法走法只提示操作者，其余只发送给本桌双方。
声音使用「方块」通道，可在 Minecraft 声音设置调整音量；更新资源后按 `F3+T`。
