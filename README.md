# Fimel Card 资源包

Minecraft Java 26.2 的 Fimel Cards 配套资源包，提供卡牌、国际象棋、中国象棋、五子棋、飞行棋、牌桌家具、字体与音效。放入客户端 `resourcepacks` 并启用；更新后按 `F3+T`。

- [数据包项目与游玩说明](https://github.com/FimelStudio/fimelcard-dp)
- [下载](https://studiofimel.com/#/works/fimel-card)

## 兼容性

以下针对 Minecraft Java 26.2，Fabric 和钠的结论来自作者实测。

| 环境 | 兼容情况 |
| --- | --- |
| 原版 | 本包的目标环境，无需额外模组 |
| Fabric | 已实测兼容 |
| 钠（Sodium） | 已实测兼容 |
| Forge | 尚未验证 |
| OptiFine | 尚未验证 |

额外光影或覆盖字体、文字着色器的资源包组合需另行验证。

## 资源来源

牌桌家具及国际象棋棋子几何使用16bit制作组的[NyaaWork喵工坊资源](https://space.bilibili.com/2907002)，原始资源归原作者所有。国际象棋另配五套棋盘、四套棋子配色；制作来源与调整记录见[棋子资源说明](.source/chess/README.md)。

中国象棋使用本项目制作的圆形棋子，棋盘与棋子均保留经典、木色两种配色，可编辑源模型见 [.source/xiangqi](.source/xiangqi/)。移动、吃子及开局／结束音来自 [Xiangqi.com 提供的下载音效](https://www.xiangqi.com/help/sounds)，来源与原文件见[音效说明](.source/xiangqi/sounds/README.md)。

五子棋提供 13／15／19 路棋盘，保留经典、木色两种棋盘与黑白圆形棋子；飞行棋提供一张传统四色棋盘、飞机及六面骰。图像与模型由本项目绘制、建模，可编辑模型及设计参考见[五子棋](.source/gomoku/README.md)、[飞行棋](.source/aeroplane_chess/README.md)，原创音效、无损源文件及生成说明见[音效来源](.source/boardgames/README.md)。
