import json
from operator import le
from rest_framework import viewsets, status
from rest_framework.response import Response
from collections import OrderedDict
from pathlib import Path
import pandas as pd
from excelParse.models import MongoDocumentReports
from excelParse.serializers import MongoDocumentReportsSerializer
from py_analytics_api import settings
from rest_framework.decorators import api_view
from py_analytics_api import ticks
import datetime
from bson import json_util, ObjectId


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


def removeSpace(string):
    return string.replace(" ", "")


def filter_existing_obj(object, listArray):
    return True if object in listArray else False


def getSearchData(value, df_column):
    dic = {}
    for index, key in enumerate(df_column):
        if (isinstance(value[index], int)):
            dic[str(key)] = float(value[index])
        else:
            dic[str(key)] = value[index]
    return dic


def getSetOnInsertData(value, df_column):
    date = datetime.datetime.strptime(value[0], "%B %Y")
    today = datetime.date.today().strftime('%Y-%m-%d')
    dic = {}
    for index, key in enumerate(df_column):
        if (isinstance(value[index], int)):
            dic[str(key)] = float(value[index])
        else:
            dic[str(key)] = value[index]
    dic['CreatedOn'] = [ticks.date_to_dotnet_tick(str(today)),0]
    dic['ModifiedOn'] = [ticks.date_to_dotnet_tick(str(today)),0]
    dic['CreatedById'] = 2
    dic['ModifiedById'] = 2
    dic['Disabled'] = False
    dic['EnabledDisabledOn'] = None
    dic['MtdMonth'] = date.month
    dic['YtdYear'] = date.year
    return dic


class ExcelParseViewSet(viewsets.ViewSet):
    # models = MongoDocumentReports
    # serializer_class = MongoDocumentReportsSerializer

    # def list(self, request):
    #     queryset = MongoDocumentReports.objects.all()
    #     serializer = MongoDocumentReportsSerializer(queryset, many=True)
    #     json_object = json.loads(json.dumps(serializer.data))

    #     # my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = Path(__file__).parent.parent
    #     # paths = os.path.join(path, "6 - CONCORD HOSPITALITY ENTERPRISES.xlsx")
    #     fn = list(Path(path).glob("*.xlsx"))[0]
    #     excel_data_df = pd.ExcelFile(fn)
    #     df = excel_data_df.parse("Channel")
    #     df_column = df.columns.values.tolist()
    #     df_list = df.values.tolist()
    #     df_column = [removeSpace(df_column[i])
    #                  for i, d in enumerate(df_column)]

    #     collection = settings.client[settings.MONGODB_DATABASES['default']
    #                                  ['name']].mongoTest
    #     listOfObject = []
    #     for value in df_list:
    #         dic = dict()
    #         for index, key in enumerate(df_column):
    #             if (isinstance(value[index], int)):
    #                 dic[str(key)] = float(value[index])
    #             else:
    #                 dic[str(key)] = value[index]
    #         # filter_existing_obj(json.dump(dic), )
    #         # new_dic = json.dumps(dic)
    #         # print(new_dic)
    #         collection.update_one(dic, {"$setOnInsert": dic})
    #         listOfObject.append(dic)

    #     # collection.insert_many(listOfObject)
    #     # collection.update_many(listOfObject, upsert=True)
    #     # queryset = MongoDocumentReports.objects.all()
    #     # serializer = MongoDocumentReportsSerializer(queryset, many=True)
    #     # json_object = json.loads(json.dumps(serializer.data))
    #     return Response(OrderedDict([
    #         ('columns', listOfObject),
    #     ]), status=status.HTTP_200_OK)

    def create(self, request):
        file = self.request.FILES['file']
        print('File: ', file.name.endswith('.xlsx'))
        if file.name.endswith('.xlsx') is False:
            raise Exception(status=status.HTTP_400_BAD_REQUEST)
        excel_data_df = pd.ExcelFile(file)
        df = excel_data_df.parse("Channel")
        df_column = df.columns.values.tolist()
        df_list = df.values.tolist()
        df_column = [removeSpace(df_column[i])
                     for i, d in enumerate(df_column)]

        collection = settings.client[settings.MONGODB_DATABASES['default']
                                     ['name']].mongoTest
        listOfObject = []
        print(len(df_list))
        for index, value in enumerate(df_list):
            searchDic = getSearchData(value, df_column)
            setOnInsertDic = getSetOnInsertData(value, df_column)
            mongoData = collection.find(searchDic)
            json_docs = [json.dumps(doc, default=CustomEncoder().default)
                         for doc in mongoData]
            if json_docs is None:
                collection.insert_one(setOnInsertDic)
            else:
                json_dict= json.loads(json_docs[0])
                collection.update_many(
                    {'_id': ObjectId(oid=json_dict['_id'])}, {"$set": setOnInsertDic})
            # json_doc = json.dumps(mongoData, default=json_util.default)
            # print('mongoData', json.loads(json_util.dumps(mongoData)))
            print('Encode', json_docs)
            # collection.insert_one(dic)

            listOfObject.append(setOnInsertDic)
            # filter_existing_obj(json.dump(dic), )
            # new_dic = json.dumps(dic)
            # print(new_dic)

        # collection.insert_many(listOfObject)
        # collection.update_many(listOfObject, upsert=True)
        # queryset = MongoDocumentReports.objects.all()
        # serializer = MongoDocumentReportsSerializer(queryset, many=True)
        # json_object = json.loads(json.dumps(serializer.data))
        return Response(OrderedDict([
            ('columns', listOfObject),
        ]), status=status.HTTP_200_OK)
        # else:
        #     return Response(OrderedDict([
        #         ('message', 'No File Found'),
        #         ('columns', []),
        #     ]), status=status.HTTP_400_BAD_REQUEST)
