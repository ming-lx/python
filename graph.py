import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

import datetime as dt
import matplotlib.dates as md

#从database文件中导入获取数据库中的数据函数
from database import select_population


def population_draw():


    日期 = []
    开盘=[]
    收盘=[]
    涨跌额=[]
    换手率=[]

    成交量 = []
    成交金额 = []
    顺序=[]
    涨跌幅=[]
    最低=[]
    最高=[]



    #调用select_population()函数获取以上列表值
    select_population(顺序,日期,开盘,收盘,涨跌额,涨跌幅, 最低,最高,成交量, 成交金额,换手率)
    最低 = list(map(float, 最低))
    成交金额 = list(map(float, 成交金额))
    成交量 = list(map(int,成交量))
    最低 = list(map(float, 最低))
    最高 = list(map(float, 最高))#因为str数据会导致坐标系混乱，因为他们不认识，所以要转换为float,int类型
    开盘 = list(map(float, 开盘))
    收盘 = list(map(float, 收盘))
    涨跌额 = list(map(float, 涨跌额))
    #换手率 = list(map(float, 换手率))

    print(顺序)
    print(日期)
    print(最低)
    print(成交金额)


    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # -------------------------------------------------
    # 开启第一个视图，
    # -------------------------------------------------
    fig1 = plt.figure('fig1')

    #设置标题
    plt.title('每日成交量')

    plt.bar( 日期,成交量, width=0.8, label=u'每日成交量', color='r')
    #设置y轴取值范围、标注
    #plt.ylim(-5, 10)
    plt.ylabel('每日成交量')
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('日期')
    #plt.xticks(日期)
    plt.xticks(rotation=60)
    #设置图例
    plt.legend(loc='upper left')
    #添加网格
    #plt.grid(b=True,axis='y',linestyle='--')


    #-------------------------------------------
    #开启第二个视图，
    #-------------------------------------------
    fig2 = plt.figure('fig2')
    #y轴显示百分数
    #fmt = '%.2f%%'
    #ytickscale = mtick.FormatStrFormatter(fmt)
    #plt.gca().yaxis.set_major_formatter(ytickscale)
    #设置折线图标题
    plt.title('每日股票最低最高时刻数据')
    #绘图
    p1, = plt.plot(日期, 最低, color = 'red')
    p2, = plt.plot(日期, 最高, color = 'blue')
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('日期')
    #plt.xticks(np.arange(20), 日期)

    #plt.yticks([0, 0.1])
    plt.xticks(rotation=60)
    #设置y轴标注
    plt.ylabel('数据')
    #添加图例
    plt.legend([p1, p2], ['最低', '最高'], loc='upper right')
    #添加网格
    plt.grid(b=True, linestyle='--')
    #plt.show()

    #-------------------------------------------
    #开启第三个视图
    #-------------------------------------------
    fig3 = plt.figure('fig3')
    #y轴显示百分数
    #fmt = '%.2f%%'
    #ytickscale = mtick.FormatStrFormatter(fmt)
    #plt.gca().yaxis.set_major_formatter(ytickscale)
    #设置折线图标题
    plt.title('每天开盘收盘情况')
    #绘图
    p1, = plt.plot(日期, 开盘, color = 'red')
    p2, = plt.plot(日期, 收盘, color = 'blue')
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('日期')
    #plt.xticks(np.arange(20), 日期)

    #plt.yticks([0, 0.1])
    plt.xticks(rotation=60)
    #设置y轴标注
    plt.ylabel('数据')
    #添加图例
    plt.legend([p1, p2], ['开盘', '收盘'], loc='upper right')
    #添加网格
    plt.grid(b=True, linestyle='--')
    #第四个视图
    fig4 = plt.figure('fig4')
    #y轴显示百分数
    #fmt = '%.2f%%'
    #ytickscale = mtick.FormatStrFormatter(fmt)
    #plt.gca().yaxis.set_major_formatter(ytickscale)
    #设置折线图标题
    plt.title('每日成交金额')
    #绘图
    p1, = plt.plot(日期, 成交金额, color = 'red')
   # p2, = plt.plot(日期, 成交量, color = 'blue')
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('日期')
    #plt.xticks(np.arange(20), 日期)

    #plt.yticks([0, 0.1])
    plt.xticks(rotation=60)
    #设置y轴标注
    plt.ylabel('成交金额')
    #添加图例
    plt.legend([p1], ['成交金额'], loc='upper right')
    #添加网格
    plt.grid(b=True, linestyle='--')
    plt.show()

