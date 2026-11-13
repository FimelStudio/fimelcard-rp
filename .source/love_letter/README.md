# 情书原创资源

宫廷角色肖像由内置 image_gen 生成，使用原创人物与服饰；未临摹商业《情书》插画。完整原图保存在 portraits_original.png，生成提示词见 prompt.txt。
十个角色按 5 列 × 2 行排列：spy、guard、priest、baron、handmaid；prince、chancellor、king、countess、princess。
生成图只负责肖像。256×384 牌面的数字、英文名、信封、封蜡、金色边框和好感标记均由确定性资源脚本绘制。
资源名使用角色英文名，不使用连续 c0 编号。物品保留 256×384 牌面；对话框和私人 HUD 使用 textures/font/love_letter/ 下的 128×192 专用字形，避免超过原版 256×256 字体图集限制。
models/ 保存可编辑 Blockbench Java 模型与嵌入纹理；牌和牌盒参照本项目 fake_card / cardbox 原有尺寸。
另有八段原创合成音效，保留 audio/ 中的无损 WAV 源文件；audio_manifest.json 记录发布 OGG 的时长及 SHA-256，来源与重建方式见 audio/README.md。
从数据包目录运行 python tools/build_love_letter_assets.py 可重建；需要 Pillow 及 Windows Georgia 字体。重建不会重新调用图像生成服务。
