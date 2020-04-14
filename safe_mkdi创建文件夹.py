import os
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("新建文件夹'%s'成功"%file_path)
    else:
        print("'%s'已经存在"%file_path)
if __name__ == "__main__":
    
    f="./jpstest/"
    ensure_dir(f)
