#!/usr/bin/env python
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager

#解决中文问题方法之一（有两种，这种更实用）
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

#基础数据
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,18,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_3 = range(1,32)
x_10 = range(51,82)

#设置图像大小
plt.figure(figsize=(20,8),dpi=100)

#绘散点图 使用scatter绘制散点图的唯一区别
plt.scatter(x_3,y_3,label = "3月份")
plt.scatter(x_10,y_10,label = "10月份")

#调整轴刻度
_x = list(x_3)+list(x_10)
_xtick_label = ["3月{}日".format(i) for i in x_3 ]
_xtick_label += ["10月{}日".format(i-50) for i in x_10 ]

#太密集的话需要改稀疏一点
plt.xticks(_x[::3],_xtick_label[::3],fontproperties = my_font,rotation=45)

#添加描述信息 fontproperties记得赋值 才能显示中文
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("3月份与10月份气温",fontproperties=my_font)
plt.legend(loc=2,prop = my_font)  #添加图例 与上面不同之处，prop

#展示
plt.show()
