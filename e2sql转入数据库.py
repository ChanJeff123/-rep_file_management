import os
import numpy as np
import pandas as pd
import  pymysql
#开启数据库连接
conn = pymysql.connect(
    user = 'root',
    host = 'localhost',
    password= '12312311',
    db = 'zkh_comnect',
    port = 3306,
)
#获取游标
cur = conn.cursor()
#此函数用来插入数据
def add_data(filename,company,name,email,address,tel,role):
    file_name_handle="zkh_2"
    # if(taxi_time=="1899-12-30 00:00:00"):
    #     return                                                                        
    sql="""insert into """ + file_name_handle +"""(company,name,email,address,tel,role) values("""+ "\"" +company +"\""+","+"\"" +name +"\""+","+"\"" +email +"\""+","+"\"" +address +"\""+","+"\"" +tel +"\""+","+"\"" +role +"\""+""")"""
    cur.execute(sql)
 
#此处获取文件所在的目录的上一级
dir=r'D:\projects\爬虫项目\企业信息\找客户db\data'
# 此处获取目录中所有的文件名称
file_name=os.listdir(dir)   
#此处获取所有的文件路径
file_dir=[os.path.join(dir,x) for x in file_name]  
#遍历所有文件开始处理Excel
for j in range(len(file_dir)):
    try:
        excel=pd.read_excel(file_dir[j])
        #删除文件的第0到第1行并且保存下来，这里如果不写inplace=True会导致文件修改不成功
        excel.drop([0,1],inplace=True)
        #将Excel的列名转换为我们需要的
        excel.columns=["company","name","email","address","tel","role","id_2"]
        #获取每列
        # id_2s=excel.iloc[:,[0]]
        companys=excel.iloc[:,[1]]
        names=excel.iloc[:,[2]]
        tels=excel.iloc[:,[3]]
        addresss=excel.iloc[:,[4]]
        emails=excel.iloc[:,[5]]
        roles=excel.iloc[:,[6]]
        #对每一列数据进行处理，从DataFrame类型转换为list类型
        # id_2s_list=id_2s.values.tolist()
        companys_list=companys.values.tolist()
        names_list=names.values.tolist()
        tels_list=tels.values.tolist()
        addresss_list=addresss.values.tolist()
        emails_list=emails.values.tolist()
        roles_list=roles.values.tolist()
        #创建对应的字符串用来存储最终数据
        # id_2s_str=''
        companys_str=''
        names_str=''
        tels_str=''
        addresss_str=''
        emails_str=''
        roles_str=''
        
        #对每一列的每一行的数据进行转换，转换为str类型
        for i in range(len(names_list)):
            # id_2s_list_index = id_2s_list[i]
            tels_list_index = tels_list[i]
            emails_list_index = emails_list[i]
            roles_list_index = roles_list[i]
            names_list_index = names_list[i]
            companys_list_index = companys_list[i]
            addresss_list_index = addresss_list[i]

            tels_str = str(tels_list_index[0]).replace('.0','').replace('+','')
            addresss_str =str(addresss_list_index[0]).replace('\"','')
            emails_str = str(emails_list_index[0])
            roles_str = str(roles_list_index[0])
            names_str = str(names_list_index[0])
            companys_str = str(companys_list_index[0])
            # id_2s_str =str(id_2s_list_index[0])
            print(file_name[j],companys_str,names_str,tels_str,file=open("outlog2.txt","a",encoding="utf-8"))
        

            #执行数据库插入操作
            try:
                add_data(file_name[j],companys_str,names_str,emails_str,addresss_str,tels_str,roles_str)
            except:
                print(addresss_str)
                pass
        conn.commit()
    except:
        pass
cur.close()
conn.close()