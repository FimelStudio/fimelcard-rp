# 卡坦岛视觉资源

地形底图与港口资源图案取自 Kenney Hexagon Pack（https://kenney.nl/assets/hexagon-pack），作者 Kenney Vleugels / Kenney，CC0-1.0，允许修改与再分发。原始 ZIP、原始 PNG 及随包许可证保留于 ../vendor/；逐文件哈希见 ../visual_manifest.json。没有复制商业 CATAN 的牌面或插图。

地形采用近邻缩放、适度降饱和与六边形遮罩。森林、丘陵、牧场、麦田、山地和沙漠分别使用原创立体树木、黏土岩层、羊群、麦穗、矿洞和仙人掌；港口含木栈桥、绳桩、货箱与帆船。几何与材质色板源为数据包 tools/catan_scenery.py，装饰并入每块地形的单个模型，中心数字与道路交点留空，不增加每棵树的展示实体。建筑、道路、海面、数字、骰面与发展牌堆同样由本项目制作。

地块数字与港口比率用朝上的薄片模型，实体 billboard 为 vertical。位置写在实体 Pos，transformation.translation 恒为零，所以不同座位的客户端可以独立转向文字，而不会让标记绕桌心漂移。发展牌堆在四／八人桌的海域外角落，牌叠和点击区域同步定位，底面独立抬高；牌背不公开开发牌顺序。

在数据包目录运行 python tools/build_catan_visual.py 重建。依赖 Pillow、NumPy 和 Windows Arial；使用本地保留的 CC0 原件，不需要再次下载。../models/ 中保存可编辑 Blockbench 源文件，纹理嵌入源模型并保留手持姿态。地形底图预览见 ../terrain_preview.png；四人桌、八人桌及两种朝向的立体模型预览见 ../board_preview_c4o0.png 等文件。预览使用实际模型面、UV、透明纹理和深度缓冲，不是游戏内截图。

拓扑只导入数据包 tools/catan_topology.py，禁止另排 ID。四/八人桌 R=.25/.35、海框 L=1.35/1.8，棋盘旋转、道路、交点、港口和骰面均共享坐标。item_display:none 的固定 Y180 由 right_rotation 抵消。顶面只有一层，数字、建筑与高亮分层，不以重复共面矩形模拟六边形。

视觉只读取公开棋面与已提交的公共动画事件，不读取玩家具体资源或未用开发牌。发牌/交易/偷牌动画使用中性袋子或统一开发牌背；真实扣费、骰值和生产仅由规则引擎决定。音效来源由独立 audio/README.md 记录，视觉导出器不会改写音频。
