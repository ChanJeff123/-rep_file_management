#-*- encoding=utf-8 -*-
'''实现批量文件转移 将文件夹 下的子目录  转移的当前目录下'''
import os
import shutil

# move files from source path to destination path 
# 从源路径下的所有文件移动到目标路径
def moveFiles(sourcePath, destPath):
	fileList = os.listdir(sourcePath)
	for file in fileList:
		filePath = os.path.join(sourcePath, file)
		#print(filePath + ' to ' + destPath)	
		shutil.move(filePath, destPath)


# 功能：将rootPath目录下所有文件夹里的文件 移动到rootPath目录下。 即把rootPath中各文件夹里的文件都移动到上一层文件夹
# 如将'D:\workspace\所有照片\2016\052.JPG' 复制到 'D:\workspace\所有照片\'
rootPath = 'D:\projects\爬虫项目\已完成项目收录\地图相关\poi\母婴\母婴全部'  #根目录
filesList = os.listdir(rootPath)   #列出根目录下的所有目录与文件
for file in filesList:
	filePath = os.path.join(rootPath, file) #拼接文件路径
	if os.path.isdir(filePath):
		#print(file)
		moveFiles(filePath, rootPath)


