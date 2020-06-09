import  pymysql
import os
import numpy as np
import pandas as pd
#开启数据库连接
conn = pymysql.connect(
    user = 'root',
    host = 'localhost',
    password= '',
    db = 'zkh_comnect',
    port = 3306,
)
cur = conn.cursor()
sql_str1 ="DROP TABLE IF EXISTS zkh_2"
cur.execute(sql_str1)
cur.execute(sql_str2)
# cur.execute(sql)
conn.commit()
cur.close()
conn