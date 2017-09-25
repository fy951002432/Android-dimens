# -gen_dpi 根据屏幕密度生成适配的px尺寸
--需配置\
--dist           生成目录\
--prefix_default 前缀 \
--suffix_default 后缀 \
--dpi_default    默认屏幕密度 240x320:120 320x480:160 480x800:240 720x1280:320	 1080x1920:480 \
--files 生成规则 \
---Describe(文件夹名称,屏幕密度[,前缀,后缀])\
-其他配置\
--start     开始数\
--end       结束数\
--distance  隔多少数去取生成源\
--accuracy  多少数算一个单位
# -运行:命令行输入-  
python gen_dpi.py

# -gen_wh 根据宽高生成适配的px尺寸
-需配置\
--dist             生成目录\
--w_prefix_default 宽前缀 \
--h_prefix_default 高前缀 \
--w_suffix_default 宽后缀 \
--h_suffix_default 高后缀 \
--files 生成规则 \
---Describe(文件夹名称,宽密度,高密度[,宽前缀,高前缀,宽后缀,高后缀])\
-其他配置\
--start     开始数\
--end       结束数\
--distance  隔多少数去取生成源\
--accuracy  多少数算一个单位
# -运行:命令行输入-   
python gen_wh.py
