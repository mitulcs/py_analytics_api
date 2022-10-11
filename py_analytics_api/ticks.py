from __future__ import print_function
import datetime
import time

# from datetime import datetime


def convert_dotnet_tick(ticks):
    """Convert .NET ticks to formatted ISO8601 time
    Args:
        ticks: integer
            i.e 100 nanosecond increments since 1/1/1 AD"""
    _date = datetime.datetime(1, 1, 1) + \
        datetime.timedelta(microseconds=ticks // 10)
    if _date.year < 1900:  # strftime() requires year >= 1900
        _date = _date.replace(year=_date.year + 1900)
    return _date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3]


def date_to_dotnet_tick(dt):
    date = datetime.datetime.strptime(dt, "%Y-%m-%d")
    tick = (date - datetime.datetime(1, 1, 1)).total_seconds() * 10000000
    return int(tick)

# def stringToDateTime(date):
#     date_time_obj = time.strptime(date, "%Y-%m-%d")
#     timestamp = time.mktime(date_time_obj)
#     date = datetime.fromtimestamp(timestamp).date()
#     # epoch = date.strftime('%s')
#     # print('epoch: ', (date.microsecond * 10 + 621355968000000000))
#     # milliseconds_since_epoch = timestamp * 1000
#     # tick = milliseconds_since_epoch * 10 + 621355968000000000
   
#     # tick = (dt - datetime.datetime(1, 1, 1)).total_seconds() * 10000000
#     return date
