import sqlite3
import datetime
#从netspyder模块中导入爬虫函数



def select_population(顺序,日期,开盘,收盘,涨跌额,涨跌幅, 最低,最高,成交量, 成交金额,换手率):
    conn = sqlite3.connect('db/gupiao.sqlite3')
    c = conn.cursor()
    # ------------------------

    # ------------------------
    for i in range(1, 20):
        c.execute('select * from historicalquote where 顺序=?', (20 - i,))
        values = c.fetchall()


        #values = c.fetchall()
        顺序.append(values[0][0])
        日期.append(values[0][1])
        开盘.append(values[0][2])
        收盘.append(values[0][3])
        涨跌额.append(values[0][4])
        涨跌幅.append(values[0][5])
        最低.append(values[0][6])
        最高.append(values[0][7])
        成交量.append(values[0][8])
        成交金额.append(values[0][9])
        换手率.append(values[0][10])




    c.close()
    conn.close()

'''
    顺序.reverse()

    #开盘.reverse()
    收盘.reverse()
    涨跌额.reverse()
    涨跌幅.reverse()
    最低.reverse()
    最高.reverse()
    成交量.reverse()
    #成交金额.reverse()
    换手率.reverse()

    #female_amount.reverse()
    #ma_scale.reverse()
    #fema_scale.reverse()'''

