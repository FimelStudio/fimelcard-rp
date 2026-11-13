# 璀璨宝石 Minecraft 主题资源

发展牌、贵族牌、桌垫与宝石袋使用 Fimel Cards 自行设计的版式，不复刻璀璨宝石原作插画。
宝石、材料、方块与生物脸部来自本机 Minecraft 26.2 客户端；权利归 Mojang / Microsoft，参与合成的原版源图保留在 vanilla/，SHA-256 见 vanilla/manifest.json。
重建优先复用 vanilla/，源图缺失时才从本机版本 jar 提取。源图只供此 Minecraft 资源包合成使用，不宣称原创或 CC0。
牌面数值来自数据包 tools/splendor_cards.json，数值引用见该文件 sources。
发展牌顶部左侧大数字与星标为分数，右侧原版宝石为永久折扣；底部原版宝石和大数字为支付花费。中部为矿洞、作坊、遗迹三类方块场景与对应颜色的材料，共 90 种牌面。
贵族使用村民、流浪商人、铁傀儡、雪傀儡、悦灵、蜜蜂、狐狸、美西螈、海龟和猪；下方要求采用发展卡轮廓，表示需要永久折扣而非支付宝石。
牌面 canonical signature 为 bonus:points:cost；相同奖励、分数、花费使用同一 canonical_id/model 和同一纹理。物品组件也应只携带这种牌的身份，不携带取得时间或牌槽，才能叠加。
预定牌物品入口位于 card:splendor/reserved/层级/牌名；本人 GUI 与第一人称显示正面，第三人称、掉落、展示框及其他上下文统一显示对应层牌背，避免暴露盲预定身份。
所有发展卡、贵族卡与牌背分别复用 `base/table`、`base/hand` 两份自定义父模型，不依赖原版生成物品父类。模型都有正反面与独立纸边，手持牌采用与 poker 一致的姿态及中心，牌面比例为 256:352；子模型仅覆盖纹理，Blockbench 源文件保留展开后的完整几何。执行 `python tools/build_splendor_assets.py --models-only --check` 可只重建这部分。
以 tier1/diamond_01 等“层级／宝石／同组序号”命名；源模型位于 models/*.bbmodel，可在 Blockbench 编辑。
纹理源位于 textures/，预览见 preview.png；所有源文件可由数据包 tools/build_splendor_assets.py 重建。
选游图标以 Minecraft 原版像素钻石、六色物品宝石和发展卡构图，保留双语铭牌。
数据包 tools/splendor_icon.svg 为可编辑布局模板，build_splendor_icon.py 将缓存的原版物品像素展开为独立 SVG 色块；
源 icon.svg（1024×1024）无外部图片依赖，导出 icon.png（256×256），仅更新22号图标与其字体切片。
首次渲染使用本机 Edge/Chromium，可设置 SPLENDOR_SVG_BROWSER 指定；未修改SVG时直接复用已提交PNG，无需浏览器。

字体 card:splendor 提供 E900～E959 发展牌、E980～E985 钻石/青金石/绿宝石/红石/煤炭/金锭图标、E986 宝石袋、E987 游戏图标、E990～E992 三层牌背、E993 分数星、EA00～EA09 贵族。
card:splendor/small 使用较小字形，card:splendor/cards 使用较大牌面；单字形切片最多 96×132，不超过 26.2 客户端 256×256 限制。

音频来源、许可和重建说明见 audio/README.md；桌面只展示公开市场、银行与贵族，不展示预约牌身份。
