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