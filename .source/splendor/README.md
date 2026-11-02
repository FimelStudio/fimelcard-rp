# 璀璨宝石原创资源

宝石、筹码、开发牌、贵族徽章、桌垫与宝石袋均为 Fimel Cards 原创程序绘制，不复用原版游戏插画、卡面或商标图。
牌面数值来自数据包 tools/splendor_cards.json，数值引用见该文件 sources。
以 tier1/diamond_01 等“层级／宝石／同组序号”命名；源模型位于 models/*.bbmodel，可在 Blockbench 编辑。
纹理源位于 textures/，预览见 preview.png；所有源文件可由数据包 tools/build_splendor_assets.py 重建。
选游图标原画为 icon.svg（1024×1024），导出 icon.png（256×256），完整保留双语铭牌；
数据包 tools/build_splendor_icon.py 可单独重建，仅处理22号图标，不覆盖其他游戏。
首次渲染使用本机 Edge/Chromium，可设置 SPLENDOR_SVG_BROWSER 指定；未修改SVG时直接复用已提交PNG，无需浏览器。

字体 card:splendor 提供 E900～E959 开发牌、E980～E985 白蓝绿红黑金筹码、E986 宝石袋、E987 游戏图标、E990～E992 三层牌背、E993 分数星、EA00～EA09 贵族。
card:splendor/small 使用较小字形，card:splendor/cards 使用较大牌面；单字形切片最多 96×132，不超过 26.2 客户端 256×256 限制。

音频来源、许可和重建说明见 audio/README.md；桌面只展示公开市场、银行与贵族，不展示预约牌身份。
