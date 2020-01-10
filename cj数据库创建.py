import  pymysql
import os
import numpy as np
import pandas as pd
#开启数据库连接
conn = pymysql.connect(
    user = 'root',
    host = 'localhost',
    password= '12312311',
    db = 'zkh_comnect',
    port = 3306,
)
#获取文件的上级目录，对应下图的路径
# dir=r'D:\projects\爬虫项目\脚本\找客户 内部软件\第二批all'
# 此处获取目录中所有的文件名称
# sql="CREATE TABLE IF NOT EXISTS zkh_1  (" \
#                     "id int(11) NOT NULL AUTO_INCREMENT COMMENT 'id序号'," \
#                     "id_2 int(11) COMMENT 'ID新'," \
#                     "company char(200) COMMENT '公司'," \
#                     "name char(200) COMMENT '联系人'," \
#                     "tel char(200) COMMENT '联系方式'," \
#                     "add char(200) COMMENT '地址'," \
#                     "email char(200) COMMENT '邮箱'," \
#                     "role char(200) COMMENT '职位', PRIMARY KEY (`id`))" \
#                     "ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8"

sql="""CREATE TABLE IF NOT EXISTS zkh_2
    ("id int(11) NOT NULL AUTO_INCREMENT COMMENT 'id序号',
    company char(40) COMMENT '公司',
    name char(20) COMMENT '联系人',
    tel char(20) COMMENT '联系方式',
    add char(200) COMMENT '地址',
    email char(20) COMMENT '邮箱',
    role char(20) COMMENT '职位',
    PRIMARY KEY (`id`)) 
    ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8"""
sql_str2="CREATE TABLE IF NOT EXISTS zkh_2 (" \
                    "id int(11) NOT NULL AUTO_INCREMENT COMMENT 'id序号'," \
                    "company char(200) COMMENT '公司'," \
                    "name char(200) COMMENT '联系人'," \
                    "email char(200) COMMENT '邮箱'," \
                    "address char(255) COMMENT '地址'," \
                    "tel char(200) DEFAULT NULL," \
                    "role char(200) DEFAULT NULL COMMENT '职位'," \
                    "PRIMARY KEY (`id`))" \
                    "ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=UTF8MB4"
cur = conn.cursor()
sql_str1 ="DROP TABLE IF EXISTS zkh_2"
cur.execute(sql_str1)
cur.execute(sql_str2)
# cur.execute(sql)
conn.commit()
cur.close()
conn