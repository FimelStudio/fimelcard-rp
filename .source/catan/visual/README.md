# 卡坦岛视觉资源

地形与自然物件取自 Kenney Hexagon Pack（https://kenney.nl/assets/hexagon-pack），作者 Kenney Vleugels / Kenney，CC0-1.0，允许修改与再分发。原始 ZIP、原始 PNG 及随包许可证保留于 ../vendor/；逐文件哈希见 ../visual_manifest.json。没有复制商业 CATAN 的牌面或插图。

地形采用近邻缩放、适度降饱和与六边形遮罩；羊群、麦穗、海面、港口标记、数字木牌、骰面及所有立体建筑和道路为本项目确定性绘制。红、蓝、白、橙棋子为 Java 原版长方体模型；城市与村庄几何不同，强盗有立体底座、身体和头部。

在数据包目录运行 python tools/build_catan_visual.py 重建。依赖 Pillow、NumPy 和 Windows Arial；使用本地保留的 CC0 原件，不需要再次下载。../models/ 中保存可编辑 Blockbench 源文件，纹理嵌入源模型。地形预览见 ../terrain_preview.png；四人桌、八人桌及两种朝向的实际模型离线预览见 ../board_preview_c4o0.png 等文件。预览使用原始模型面、UV、透明纹理和深度缓冲，属于资产检查图，不是游戏内截图。

拓扑只导入数据包 tools/catan_topology.py，禁止另排 ID。四/八人桌 R=.25/.35、海框 L=1.35/1.8，棋盘旋转、道路、交点、港口和骰面均共享坐标。item_display:none 的固定 Y180 由 right_rotation 抵消。顶面只有一层，数字、建筑与高亮分层，不以重复共面矩形模拟六边形。

视觉只读取公开棋面与已提交的公共动画事件，不读取玩家具体资源或未用开发牌。发牌/交易/偷牌动画使用中性袋子或统一开发牌背；真实扣费、骰值和生产仅由规则引擎决定。音效来源由独立 audio/README.md 记录，视觉导出器不会改写音频。
