import sqlite3
import time
DB_FILES = 'db/gupiao.sqlite3'
# 初始化数据库
def init_db():
    # 创建数据库连接
    conn = sqlite3.connect(DB_FILES)

    try:
        sql = '''
            CREATE TABLE IF NOT EXISTS historicalquote (
                顺序  INTEGER PRIMARY KEY   AUTOINCREMENT,
                日期  TEXT ,
                开盘 TEXT,
                收盘 TEXT,
                涨跌额 TEXT,
                涨跌幅 TEXT,
                最低 TEXT,
                最高  TEXT,
                成交量 TEXT,
                成交金额 TEXT,
                换手率  TEXT

                )
        '''
        conn.execute(sql)
        print('数据库初始化成功')
    except:
        print('数据库初始化失败')
    finally:
        # 关闭数据库连接
        conn.close()



