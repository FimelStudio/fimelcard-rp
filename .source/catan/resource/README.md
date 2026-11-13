# 卡坦岛资源牌

五种资源使用 Fimel Card 原创像素图案：木材为双木段，砖块为红砖堆，羊毛为浅色毛线团，粮食为金色麦穗，矿石为带浅色矿脉的灰色矿块。

砖块港和羊毛港采用同样的红砖堆、浅色毛线团，移除方框底色并放大到 72×72，分别使用红色、绿色圆框。`2:1` 与资源图案分区显示；总览见 `../ports-preview.png`。在数据包仓库执行 `python tools/build_catan_visual.py --ports-only` 可同步运行纹理、Blockbench 工程与四种棋盘预览。
资源牌不再裁切港口圆牌；图案在 32×32 逻辑像素上绘制，以整数倍近邻放大到 64×64，避免非等比拉伸与港口圆框残角。
深色轮廓、不同底色与大面积剪影用于改善小字号下的辨认；颜色不是唯一识别依据。

在数据包仓库运行 `python tools/build_catan_visual.py --resources-only` 后，运行 `python tools/build_catan_font.py` 同步对话框图片字体。
资源字体保留原有字形编号、显示高 14 和 ascent 12，桌面飞行资源物品保留原有 item_model 路径。
可编辑模型见 `../models/resource/*.bbmodel`，其嵌入纹理与发布 PNG 同步；`manifest.json` 保存纹理哈希。
`preview.png` 上排为放大图，下排为实际 14 像素图标的三倍近邻检查图，不是游戏截图。
