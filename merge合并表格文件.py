# -*- coding: utf-8 -*-
# coding:utf-8

#合并完最多65536行  多的话就选择import openpyxl
import xlrd
import os
import xlwt
from xlutils.copy import copy

"""
将文件夹下所有excel文件合并成一个文件
注意：
    本代码仅支持合并excel文件第一个sheet，如果合并的excel文件有多个sheet，只会读取和合并第一个sheet,
    需要合并的excel文件如果有多个sheet需要修改代码的merge_excel()函数
思路：
    1.获取路径下所有文件，注意 本代码没有异常处理
    2.新建一个excel文件，用于存储全部数据
    3.逐个打开需要合并的excel文件，逐行读取数据，再用一个列表来保存每行数据。最后该列表中会存储所有的数据
    4.向excel文件中逐行写入
"""


def get_allfile_msg(file_dir):
    for root, dirs, files in os.walk(file_dir):
        '''
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件 
        '''
        return root, dirs, [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]


def get_allfile_url(root, files):
    """
    将目录的路径加上'/'和文件名，组成文件的路径
    :param root: 路径
    :param files: 文件名称集合
    :return: none
    """
    allFile_url = []
    for file_name in files:
        file_url = root + '/' + file_name
        allFile_url.append(file_url)
    return allFile_url


def all_to_one(root, allFile_url, file_name='allExcel.xls', title=None, have_title=True):
    """
    合并文件
    :param root: 输出文件的路径
    :param allFile_url: 保存了所有excel文件路径的集合
    :param file_name: 输出文件的文件名
    :param title: excel表格的表头
    :param have_title: 是否存在title(bool类型),默认为true，不读取excel文件的第0行
    :return: none
    """
    # 首先在该目录下创建一个excel文件,用于存储所有excel文件的数据
    file_name = root + '/' + file_name
    create_excel(file_name, title)

    list_row_data = []
    for f in allFile_url:
        # 打开excel文件
        print('打开%s文件' % f)
        excel = xlrd.open_workbook(f)
        # 根据索引获取sheet，这里是获取第一个sheet
        table = excel.sheet_by_index(0)
        print('该文件行数为：%d，列数为：%d' % (table.nrows, table.ncols))

        # 获取excel文件所有的行
        for i in range(table.nrows):
            # 如果存在表头，则跳过第0行，否则不跳过
            if have_title and i == 0:
                continue
            else:
                row = table.row_values(i)  # 获取整行的值，返回列表
                list_row_data.append(row)

    print('总数据量为%d' % len(list_row_data))
    # 写入all文件
    add_row(list_row_data, file_name)


# 创建文件名为file_name,表头为title的excel文件
def create_excel(file_name, title):
    print('创建文件%s' % file_name)
    a = xlwt.Workbook()
    # 新建一个sheet
    table = a.add_sheet('sheet1', cell_overwrite_ok=True)
    # 写入数据
    for i in range(len(title)):
        table.write(0, i, title[i])
    a.save(file_name)


# 向文件中添加n行数据
def add_row(list_row_data, file_name):
    # 打开excel文件
    allExcel1 = xlrd.open_workbook(file_name)
    sheet = allExcel1.sheet_by_index(0)
    # copy一份文件,准备向它添加内容
    allExcel2 = copy(allExcel1)
    sheet2 = allExcel2.get_sheet(0)

    # 写入数据
    i = 1
    for row_data in list_row_data:
        for j in range(len(row_data)):
            sheet2.write(sheet.nrows + i, j, row_data[j])
        i += 1
    # 保存文件，将原文件覆盖
    allExcel2.save(file_name)
    print('合并完成')


if __name__ == '__main__':
    # 设置文件夹路径

    file_dir = r'D:\projects'
    # 获取文件夹的路径,该路径下的所有文件夹，以及所有文件
    root, dirs, files = get_allfile_msg(file_dir)
    # 拼凑目录路径+文件名,组成文件的路径,用一个列表存储
    allFile_url = get_allfile_url(root, files)
    # 设置文件名，用于保存数据
    file_name = 'all.xls'
    # 设置excle文件表头
    title = ['a', 'b', 'c', 'd']
    # have_title参数默认为True,为True时不读取excel文件的首行
    all_to_one(root, allFile_url, file_name=file_name, title=title, have_title=True)
    print('ok')