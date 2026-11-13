# 卡坦岛对话框图片字体

字体为 `card:catan`，仅用于卡坦岛 Dialog 内的资源及开发牌图标，不修改其他游戏字体。
木材、砖块、羊毛、粮食、矿石复用本资源包现有资源牌图案；五种开发牌图标由 Fimel Card 原创。
源路径、源文件 SHA-256 和字形映射保存在 `manifest.json`。

在数据包仓库依次执行：

```powershell
python tools/build_catan_visual.py
python tools/build_catan_font.py
python tools/build_catan_ui.py
python tools/test_catan_ui.py --java <Java25路径>
```

单图标 32×32 像素，显示高 14、ascent 12；低于原版 256×256 单字形限制。
图标组件显式使用白色，旁边的中文与数字仍使用默认字体；多行图标之间留空行，避免挤压。
四列交易按钮每列 110 像素，其他菜单按钮 145 像素。
服务端回归会执行 Dialog 宏、检查字体切片与生成幂等；游戏客户端仍需检查实际显示和点击尺寸。
