# 二维码生成工具

# 二维码本质上就是一段字符串
# 我们可以把任意的字符串，制作成一个二维码图片
# 生活中使用的二维码，更多的是一个URL（网址）

# 标准库里面能不能干这件事情？好像没有这个功能
# 这时候就要看第三方库了——搜索引擎——qrcode

import qrcode

img = qrcode.make('艾莉丝努力练剑！')
# img = qrcode.make('艾莉丝努力练剑！秃秃，新的一周，继续加油吧！艾莉丝会一直支持你哒！')
img.save('qrcode.png')
# no news is good news