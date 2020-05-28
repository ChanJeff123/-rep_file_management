import time
import datetime
ctime10=str(int(round(time.time())))
ctime13=str(int(round(time.time() * 1000)))
ctime16=str(int(round(time.time() * 1000000)))
ctime18=str(int(round(time.time() * 100000000)))

# 13位 当天0点
t = time.localtime(time.time())
time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S'))
et=int(time1)*1000
st=et-86400000
print(st,et)

print(ctime10)
print(ctime13)
print(ctime16)
print(ctime18)

now1=datetime.datetime.now()
hour_now=now1.strftime('%H')
today = datetime.date.today()
oneday=datetime.timedelta(days=1) 
yesterday=today-oneday
# table="huya_{}".format(yesterday).replace("-","")
print(now1)
print(hour_now)
print(today)
print(yesterday)


timestamp = 1462451334
#转换成localtime
time_local = time.localtime(timestamp)
print(time_local)


 
 
from datetime import datetime
 
def timestamp_to_strtime(timestamp):
 
    """将 13 位整数的毫秒时间戳转化成本地普通时间 (字符串格式)
    :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
    :return: 返回字符串格式 {str}'2016-02-25 20:21:04.242000'
    """
    
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    return local_str_time
 
def timestamp_to_datetime(timestamp):
 
    """将 13 位整数的毫秒时间戳转化成本地普通时间 (datetime 格式)
    :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
    :return: 返回 datetime 格式 {datetime}2016-02-25 20:21:04.242000
    """
    
    local_dt_time = datetime.fromtimestamp(timestamp / 1000.0)
    
    return local_dt_time
    
def datetime_to_strtime(datetime_obj):
    
    """将 datetime 格式的时间 (含毫秒) 转为字符串格式
    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: {str}'2016-02-25 20:21:04.242'
    """
    
    local_str_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    
    return local_str_time
 
def datetime_to_timestamp(datetime_obj):
    
    """将本地(local) datetime 格式的时间 (含毫秒) 转为毫秒时间戳
    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: 13 位的毫秒时间戳 1456402864242
    """
    
    local_timestamp = long(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    
    return local_timestamp
 
def strtime_to_datetime(timestr):
 
    """将字符串格式的时间 (含毫秒) 转为 datetiem 格式
    :param timestr: {str}'2016-02-25 20:21:04.242'
    :return: {datetime}2016-02-25 20:21:04.242000
    """
    
    local_datetime = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f")
    
    return local_datetime
 
def strtime_to_timestamp(local_timestr):
 
    """将本地时间 (字符串格式，含毫秒) 转为 13 位整数的毫秒时间戳
    :param local_timestr: {str}'2016-02-25 20:21:04.242'
    :return: 1456402864242
    """
    
    local_datetime = strtime_to_datetime(local_timestr)
    
    timestamp = datetime_to_timestamp(local_datetime)
    
    return timestamp
 
def current_datetime():
    
    """返回本地当前时间, 包含datetime 格式, 字符串格式, 时间戳格式
    :return: (datetime 格式, 字符串格式, 时间戳格式)
    """
    
    # 当前时间：datetime 格式
    
    local_datetime_now = datetime.now()
    
    # 当前时间：字符串格式
    
    local_strtime_now = datetime_to_strtime(local_datetime_now)
    
    # 当前时间：时间戳格式 13位整数
    
    local_timestamp_now = datetime_to_timestamp(local_datetime_now)
    
    return local_datetime_now, local_strtime_now, local_timestamp_now
