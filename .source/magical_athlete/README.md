# 胡闹运动会原创资源

本目录保留 Fimel Cards 原创体育场、36 个不同几何的立体角色、六面骰、骰盅、奖杯与道具模型的纹理、可编辑 Blockbench 工程及预览。角色依照身份分别设计成动物、人物或物件，不使用 CMYK 的官方插画、商标图或角色牌面。

- `boards-preview.png`：日间橙红／夜间紫蓝两面体育场，带立体看台、护栏和灯塔；四人桌与八人桌共用模型，分别缩放至 2.7／3.6 格。
- `racers-preview.png`：36 位角色的中文名、资源名和实际立体棋子缩略图；游戏中不再使用角色牌。
- `guess-preview.png`：天才预测使用的六张独立骰面，快捷栏同时显示 1～6，第七格不预测，不需要翻页。
- `figures-preview.png`：从实际长方体几何绘制的 36 个立体棋子等距预览。
- `figures.json`：各角色几何签名、脚底基准和手持姿态。

立体棋子生成时会切除方块交集，由后添加的装饰保留交集配色，并裁去全部内部面及部分遮挡面的重叠区域，避免帽子、披风、爱心等部件产生共面闪烁。桌面、手持和可编辑源模型使用同一份清理后的几何；资产测试覆盖体积、配色和共面检查。
- `props-preview.png`：骰子、积分、金银奖牌、旗帜、绊倒、传送、火箭、爱心、奖杯、菜单和香蕉。
- `models/`：每个运行模型对应的 `.bbmodel`，内嵌纹理，可直接用 Blockbench 打开。
- `asset-map.json`／`font-map.json`：运行资源 ID、格心、骰子面向与 Unicode 图片字体映射。

赛道规则来自原作，体育场外观重新绘制。唯一格心数据为数据包 `tools/magical_athlete_track.json` 的 `layout.positions`（16×16 模型单位，0 起点、30 终点；第 15 格为第二转角），纹理与运行棋子从同一份格心定位。改棋盘尺寸必须一起重建，不得再独立手写坐标。

`card:magical_athlete/racer/<英文名>`、`token/<英文名>`、`hand/<英文名>` 均为同一角色的完整立体模型。模型脚底统一为 Y=8，中心 X/Z=8；桌面 `none` 不受手持姿态影响，缩小时不会下沉。招募脚底为桌面控制器上方 1.055 格，比赛脚底为 1.052 格，同格多人横向错开并缩小。秘密阵容在物品栏和本人第一人称显示角色，第三人称和掉落视角显示通用问号模型。骰子上 1 下 6、北 2 南 5、东 3 西 4，对面合计 7。

文本图片字体为 `magical_athlete:icons`：角色从 U+E200 至 U+E223，按 0～35 号对应；道具从 U+E100 至 U+E10B。头像字高 22、上升 19；道具字高 16、上升 13。每个单字图像只有 64×64，不依赖系统中文字体显示图案。

在数据包根目录运行 `python tools/build_magical_athlete_assets.py` 重建，依赖 Pillow；仅重建立体角色可运行 `python tools/build_magical_athlete_figures.py`。改动几何或桌面位置后还需运行 `python tools/build_direct_interactions.py --game magical_athlete`。音乐和音效原件、作曲源说明与许可见 `audio/`，独立重建器为 `build_magical_athlete_sound.py`。本项目原创图像／模型使用与仓库一致的许可；音频单独按其 CC0 声明。
