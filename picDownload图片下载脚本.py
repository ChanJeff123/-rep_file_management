import requests
import os
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
def downloadp(link,filename,file_path):
    try:
        pic = requests.get(link, headers=headers)
        if pic.status_code == 200:
            with open(os.path.join(file_path)+os.sep+filename, 'wb') as fp:
                fp.write(pic.content)
                fp.close()
        print ("下载完成")
    except Exception as e:
        print (e)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("新建文件夹'%s'成功"%file_path)
    else:
        print("'%s'已经存在"%file_path)
if __name__ == "__main__":
    f="./jpg/"
    ensure_dir(f)
    url="https://sta-op.douyucdn.cn/dycatr/a184836e114db124347b36b702a17638.png"
    name="cs.jpg"
    downloadp(url,name,f)
