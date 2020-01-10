# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json
 
def youdao(English):
    Request_URL='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    From_Data={}
    # From_Data['type']=AUTO
    From_Data['i']=English
    From_Data['from']='AUTO'
    From_Data['to']='AUTO'
    From_Data['smartresult']='dict'
    From_Data['client']='fanyideskweb'
    From_Data['salt']='1525344419877'
    From_Data['sign']='721bbfed345b0d955d8691221ed2b1e1'
    From_Data['doctype']='json'
    From_Data['version']='2.1'
    From_Data['keyfrom']='fanyi.web'
    From_Data['action']='FY_BY_REALTIME'
    From_Data['typoResult']='false'
    data=parse.urlencode(From_Data).encode('utf-8')
 #当字符串数据以url的形式传递给web服务器时,字符串中是不允许出现空格和特殊字符，因此我们需要转化格式
    response=request.urlopen(Request_URL,data)
#urlopen是urlopen里的一个方法函数通过网址URL来获取数据：urlopen(url, data=None, proxies=None)
#参数 url 表示远程数据的路径，一般是 http 或者 ftp 路径。
#参数 data 表示以 get 或者 post 方式提交到 url 的数据。
#参数 proxies 表示用于代理的设置
    html=response.read().decode('utf-8')
    translate_results=json.loads(html) #将json字符串编码为python对象
    translate_results = translate_results['translateResult'][0][0]['tgt'] #找到翻译结果，由translate的结果而来
    print(translate_results)
if __name__ == "__main__":
    youdao('where are you')