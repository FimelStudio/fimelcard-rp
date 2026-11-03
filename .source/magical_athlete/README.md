# 胡闹运动会原创资源

本目录保留 Fimel Cards 原创体育场、36 枚角色头像立牌、同款平放徽章、六面骰、骰盅、奖杯与道具模型的纹理、可编辑 Blockbench 工程及预览。角色用鲜明的物件／动物徽章区分，不使用 CMYK 的官方插画、商标图或角色牌面。

- `boards-preview.png`：温和／狂野两面；四人桌与八人桌共用纹理，分别缩放至 2.7／3.6 格。
- `racers-preview.png`：36 位角色的中文名、资源名和头像对照。
- `props-preview.png`：骰子、积分、金银奖牌、旗帜、绊倒、传送、火箭、爱心、奖杯、菜单和香蕉。
- `models/`：每个运行模型对应的 `.bbmodel`，内嵌纹理，可直接用 Blockbench 打开。
- `asset-map.json`／`font-map.json`：运行资源 ID、格心、骰子面向与 Unicode 图片字体映射。

赛道规则来自原作，体育场外观重新绘制。唯一格心数据为数据包 `tools/magical_athlete_track.json` 的 `layout.positions`（16×16 模型单位，0 起点、30 终点；第 15 格为第二转角），纹理与运行棋子从同一份格心定位。改棋盘尺寸必须一起重建，不得再独立手写坐标。

`card:magical_athlete/racer/<英文名>` 为带圆形头像的立牌，`token/<英文名>` 为平放圆形徽章。骰子上 1 下 6、北 2 南 5、东 3 西 4，对面合计 7。默认手持缩小，桌面投骰动画使用 `none` 模式并按服务器已锁定点数旋转。

文本图片字体为 `magical_athlete:icons`：角色从 U+E200 至 U+E223，按 0～35 号对应；道具从 U+E100 至 U+E10B。头像字高 22、上升 19；道具字高 16、上升 13。每个单字图像只有 64×64，不依赖系统中文字体显示图案。

在数据包根目录运行 `python tools/build_magical_athlete_assets.py` 重建，依赖 Pillow。音乐和音效原件、作曲源说明与许可见 `audio/`，独立重建器为 `build_magical_athlete_sound.py`。本项目原创图像／模型使用与仓库一致的许可；音频单独按其 CC0 声明。
