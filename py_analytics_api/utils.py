from pymongo import MongoClient
import json
from bson import json_util, ObjectId
import datetime
import calendar

def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                         )
    db_handle = client[db_name]
    return db_handle, client

def getMonthEndDate(firstMonthStartDate):
    lastDayOfMonth = calendar.monthrange(firstMonthStartDate.year, firstMonthStartDate.month)[1]
    firstMonthEndDate = datetime.datetime(firstMonthStartDate.year, firstMonthStartDate.month, lastDayOfMonth,23,59,59)
    return firstMonthEndDate

def getYearEndDate(firstYearStartDate):
    firstYearEndDate = datetime.datetime(firstYearStartDate.year,12,31,23,59,59)
    return firstYearEndDate

class CustomEncoder(json.JSONEncoder):
    """A C{json.JSONEncoder} subclass to encode documents that have fields of
    type C{bson.objectid.ObjectId}, C{datetime.datetime}
    """

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
