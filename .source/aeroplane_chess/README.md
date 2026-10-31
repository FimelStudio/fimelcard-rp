# 飞行棋原创资源

棋盘图像、飞机、六面骰由 Fimel Cards 绘制/建模。模型为原版 Java 方块元素，保留可编辑 Blockbench 文件。
棋盘布局借鉴传统实体飞行棋的折角跑道、四角机场和彩色终点，参考 [AlbertNi 的 Aeroplane Chess 棋盘展示](https://steamcommunity.com/sharedfiles/filedetails/?id=2131170438)。本项目重新绘制，未直接使用该展示图片。
从数据包目录运行 `python tools/build_aeroplane_visual.py` 重建，依赖 Pillow。
路径唯一来源为 `tools/aeroplane_path.json`，先运行 `tools/build_aeroplane_game.py` 更新规则路径。
四人桌棋盘边长2.7，八人桌3.6。传统17单位模板缩放到15单位版面；52个外环色格、机场、起飞位、六格终点均在路径表中定义，绘图与实体读取同一份坐标，方向旋转同步模型、路径和命中区。
六面骰上1下6、北2南5、东3西4；动画目标只读取服务器已锁定点数，所有对面点数相加为7。
飞机沿普通路径逐格低跳，起飞抬升、跳格跃起、飞越提高航线、撞机6刻返回本方机场。
仅生成16架以内飞机和对应命中区；停用颜色不生成模型。叠放飞机轻微错位，也可用Q菜单选择编号。
