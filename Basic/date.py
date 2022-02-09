import calendar
import datetime

today = datetime.date.today()
todaydetail = datetime.datetime.today()

# 今日の日付
print('-------------------')
print(today)
print(todaydetail)

# 今日の日付：それぞれの値
print('-------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

# 日付のフォーマット
print('-------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y%m%d %H:%M:%S"))

# 明日の日付
print(today + datetime.timedelta(days=1))

newyear = datetime.datetime(2022, 1, 1)
print(newyear + datetime.timedelta(days=7))

# うるう年の判定
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

print(calendar.leapdays(2010, 2022))
