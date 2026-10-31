# UNO 美术源文件与导出

`art-atlas.png` 为本次使用图像生成工具绘制的原始艺术源图，分成四个平面像素风面板：左上为空白红色牌面与象牙白斜椭圆，右上为黑底 UNO 牌背，左下为红色 UNO 牌盒正面，右下为四色斜纹侧面。

生成提示词摘要：`2x2 pixel-art UNO flat texture atlas, four panels front blank red ellipse / black UNO back / red UNO box / colored stripe side, ivory borders, crisp downsample, no perspective`。

`export_assets.py` 使用 Pillow 裁切原图、对红色牌面换色，并叠加精确的像素数字、跳过、反转、+2、四色变色与 +4 符号。没有用手绘占位纹理替代源图。重新导出：

```shell
python .source/uno/export_assets.py
```

也可通过 `--art <路径>` 导入新的同布局源图；首次生成所用原图已复制到本目录。导出会覆盖 UNO 专属运行资产，其他游戏不受影响。

- 所有物品纹理均为 48×48，沿用 `card:item/fake_card` 与 `card:item/cardbox` 几何。
- 卡牌正面 UV 主区是 `[4,2]～[30,46]`，正反纹理分别绑定 `#0` 与 `#1`。
- 原 `fake_card` 的 south 面横向 UV 是 `10→1.33333`，会镜像文字。导出器额外生成 `back_flipped.png`：仅将牌背主区水平预翻转，所有 UNO 卡片模型的 `#1` 绑定该纹理；`#0` 和 `back` 物品前面仍使用正常方向的 `back.png`。这样两侧的 UNO 字母均正常，不改变共享几何或其他游戏。
- 牌盒正面主区是 `[2,0]～[32,48]`，两侧使用 `[42,0]～[48,48]`。
- 资源名以 `r`、`y`、`g`、`b` 表示红、黄、绿、蓝，后接 `0～9`、`skip`（跳过）、`reverse`（反转）、`plus2`（+2），例如红色 7 为 `r7`、蓝色跳过为 `bskip`。两张黑色牌分别为 `wild`、`wild_plus4`；牌背与牌盒仍为 `back`、`box`。
- 后台牌型编号仍为 0～53，导出器 `asset_name()` 负责映射可读资源名；0～51 依次为红、黄、绿、蓝，每色 0～9、跳过、反转、+2，52 为变色、53 为变色 +4。
- `card:uno/dialog` 对应 U+E600～U+E635，高度 54、ascent 50，每张牌一个位图字形；高度与斗地主选牌面板六片各 9px 拼成的完整牌接近。Dialog 每行八个牌型，行间隔 63px；独立 HUD 字体的尺寸不受影响。
- `card:uno/dialog_selected` 使用同一字符范围和尺寸，引用 `textures/font/uno/selected/` 中带金黄亮框的牌面；选中／取消只切字体，牌面尺寸与排列不变。HUD 的选中牌面也复用这些 PNG。
- HUD 普通／亮框字形分别为 U+E600～U+E635 与 U+E700～U+E735。`card:uno/hud` 与 `hud_dense` 的高度和 ascent 均为 56，接近斗地主手牌；牌型超过 18 种时改用高度 40 的 `hud_medium` 分两行，超过 36 种时改用高度 32 的 `hud_small` 分三行。四种字体各有对应的 `_neg` 负宽字体，由数据包的 `python tools/build_uno_hud.py` 生成，复用上述 PNG，不修改上游 BetterTitle 或全局字体。数量独立位于牌下方，留出 5 GUI 像素间距，避开物品名称；最宽一行不超过 306 GUI 像素。BetterTitle 正 Y 向上，底行牌面／数量为 12／0，多行向上延伸。
- `selection-preview.png` 并排显示普通牌面与选中亮框，供检查选中状态，不参与游戏运行。
- `contact-sheet.png` 是导出后的检查预览，不参与游戏运行。

Skip 的中心符号为原生 15×15 像素、角标为独立 9×9 像素；圆环和斜杠使用单像素线条，保留内部空隙。Reverse 的中心为 17×17 像素、双箭之间保留留白，角标另绘 9×9 细箭头。6／9 在中心及双角数字下加横线；中心留两像素间隔，角标留一像素间隔，右下角整体旋转后仍保持读向正确。上述细节由 `action_icon()`、`underline_digit()` 和 `make_face()` 控制，重导出时保留。

图案中的 UNO 名称仅用于辨认游戏。运行包无需包含本目录、导出脚本或 Pillow。
