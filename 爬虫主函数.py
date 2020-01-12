from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import hashlib
import os
import re
import logging
import sqlite3
import time
import threading
import datetime
import 建立数据库
from graph import population_draw
建立数据库.init_db()




logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validateUpdate(html):
    """验证数据是否更新，更新返回True，未更新返回False"""
    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):  # 如果文件存在读取文件内容
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        # 把新的md5码写入到文件中
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True

def insert_hisq_data(row):
    """在股票历史价格表中传入数据"""
    # 1. 建立数据库连接
    # 创建数据库连接
    conn = sqlite3.connect('db/gupiao.sqlite3')
    try:
        # 1.创建游标对象
        cursor = conn.cursor()
        # 2.执行SQL操作
        sql = '''insert into historicalquote(日期, 开盘, 收盘, 涨跌额, 涨跌幅, 最低, 最高, 成交量, 成交金额, 换手率)values (?,?,?,?,?,?,?,?,?,?)'''
        affectedcount = cursor.execute(sql,[row['日期'],row['开盘'],row['收盘'],row['涨跌额'],row['涨跌幅'],row['最低'],row['最高'],row['成交量'],row['成交金额'],row['换手率']])
        logger.debug('影响的数据行数{0}'.format(affectedcount))
        # 3. 提交数据库事物
        conn.commit()
    except sqlite3.DatabaseError as error:
        # 4. 回滚数据库事物
        conn.rollback()
        logger.debug('插入数据失败' + error)
    finally:
        # 5. 关闭数据连接
        conn.close()


# 线程运行标志
isrunning = True
# 爬虫工作间隔
interval = 5


def controlthread_body():
    """控制线程体函数"""

    global interval, isrunning

    while isrunning:
        # 控制爬虫工作计划
        i = input('输入#终止爬虫，输入数字改变爬虫工作间隔，单位秒：')
        logger.info('控制输入{0}'.format(i))
        try:
            interval = int(i)
        except ValueError:
            if i.lower() == '#':
                isrunning = False


def workthread_body():
    global interval, isrunning
    while isrunning:
        logger.info('爬虫开始工作...')


        driver =webdriver.Chrome()

        driver.get('http://q.stock.sohu.com/cn/000018/lshq.shtml')
        a = driver.find_element_by_id('BIZ_hq_historySearch')
        if validateUpdate(a.text):  # 数据更新
            data = []
            print(a.text)
            rows = re.split(r'\s+', a.text)
            print(rows)
            print(rows[0:19])
            gupiao=rows[19:]
            row_num = int(len(gupiao) / 10)
            for i in range(0, row_num):
                fields = {}
                fields['日期'] = gupiao[0 + i * 10]
                fields['开盘'] = gupiao[1 + i * 10]
                fields['收盘'] = gupiao[2 + i * 10]
                fields['涨跌额'] = gupiao[3 + i * 10]
                fields['涨跌幅'] = gupiao[4 + i * 10]
                fields['最低'] = gupiao[5 + i * 10]
                fields['最高'] = gupiao[6 + i * 10]
                fields['成交量'] = gupiao[7 + i * 10]
                fields['成交金额'] = gupiao[8 + i * 10]
                fields['换手率'] = gupiao[9+ i * 10]
                data.append(fields)
            print(data)
            for row in data:

               insert_hisq_data(row)

        driver.quit()
        population_draw()


        logger.info('爬虫休眠{0}秒...'.format(interval))
        time.sleep(interval)

def main():
    """主函数"""
    global interval, isrunning
    # 创建工作线程对象workthread
    workthread = threading.Thread(target=workthread_body, name='WorkThread')
    # 启动线程workthread
    workthread.start()

    # 创建控制线程对象controlthread
    controlthread = threading.Thread(target=controlthread_body, name='ControlThread')
    # 启动线程controlthread
    controlthread.start()



if __name__ == '__main__':
    main()

