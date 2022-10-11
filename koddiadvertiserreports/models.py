from django.db import models
from mongoengine import fields, Document


class KddiAdvertiserReports(Document):
    id = fields.ObjectId()
    createdOn = fields.ListField(db_field='CreatedOn')
    createdById = fields.IntField(db_field='CreatedById')
    modifiedOn = fields.ListField(db_field='ModifiedOn')
    modifiedById = fields.IntField(db_field='ModifiedById')
    disabled = fields.BooleanField(db_field='Disabled')
    enabledDisabledOn = fields.StringField(db_field='EnabledDisabledOn')
    reportDate = fields.ListField(db_field='ReportDate')
    propertyId = fields.IntField(db_field='PropertyId')
    mediaChannel = fields.StringField(db_field='MediaChannel')
    clicks = fields.IntField(db_field='Clicks')
    avgCPC = fields.StringField(db_field='AvgCPC')
    spend = fields.StringField(db_field='Spend')
    bookings = fields.IntField(db_field='Bookings')
    totalBookings = fields.IntField(db_field='TotalBookings')
    rn = fields.IntField(db_field='RN')
    totalRN = fields.IntField(db_field='TotalRN')
    revenue = fields.StringField(db_field='Revenue')
    totalRevenue = fields.StringField(db_field='TotalRevenue')
    gre = fields.StringField(db_field='GRE')
    totalGRE = fields.StringField(db_field='TotalGRE')
    koddiFileId = fields.StringField(db_field='koddiFileId')
    status = fields.IntField(db_field='status')
    impressions = fields.IntField(db_field='Impressions')

    meta = {'collection': 'koddiadvertiserreports'}


# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = KddiAdvertiserReportsResponsefromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class KddiAdvertiserReportsResponseElement:
    enabledDisabledOn: None
    id: Optional[str] = None
    createdOn: Optional[List[float]] = None
    createdById: Optional[int] = None
    modifiedOn: Optional[List[float]] = None
    modifiedById: Optional[int] = None
    disabled: Optional[bool] = None
    reportDate: Optional[List[float]] = None
    propertyId: Optional[int] = None
    mediaChannel: Optional[str] = None
    clicks: Optional[int] = None
    avgCPC: Optional[str] = None
    spend: Optional[str] = None
    bookings: Optional[int] = None
    totalBookings: Optional[int] = None
    rn: Optional[int] = None
    totalRN: Optional[int] = None
    revenue: Optional[str] = None
    totalRevenue: Optional[str] = None
    gre: Optional[str] = None
    totalGRE: Optional[str] = None
    koddiFileId: Optional[str] = None
    status: Optional[int] = None
    impressions: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'KddiAdvertiserReportsResponseElement':
        assert isinstance(obj, dict)
        enabledDisabledOn = from_none(obj.get("enabledDisabledOn"))
        id = from_union([from_str, from_none], obj.get("id"))
        createdOn = from_union([lambda x: from_list(from_float, x), from_none], obj.get("createdOn"))
        createdById = from_union([from_int, from_none], obj.get("createdById"))
        modifiedOn = from_union([lambda x: from_list(from_float, x), from_none], obj.get("modifiedOn"))
        modifiedById = from_union([from_int, from_none], obj.get("modifiedById"))
        disabled = from_union([from_bool, from_none], obj.get("disabled"))
        reportDate = from_union([lambda x: from_list(from_float, x), from_none], obj.get("reportDate"))
        propertyId = from_union([from_int, from_none], obj.get("propertyId"))
        mediaChannel = from_union([from_str, from_none], obj.get("mediaChannel"))
        clicks = from_union([from_int, from_none], obj.get("clicks"))
        avgCPC = from_union([from_str, from_none], obj.get("avgCPC"))
        spend = from_union([from_str, from_none], obj.get("spend"))
        bookings = from_union([from_int, from_none], obj.get("bookings"))
        totalBookings = from_union([from_int, from_none], obj.get("totalBookings"))
        rn = from_union([from_int, from_none], obj.get("rn"))
        totalRN = from_union([from_int, from_none], obj.get("totalRN"))
        revenue = from_union([from_str, from_none], obj.get("revenue"))
        totalRevenue = from_union([from_str, from_none], obj.get("totalRevenue"))
        gre = from_union([from_str, from_none], obj.get("gre"))
        totalGRE = from_union([from_str, from_none], obj.get("totalGRE"))
        koddiFileId = from_union([from_str, from_none], obj.get("koddiFileId"))
        status = from_union([from_int, from_none], obj.get("status"))
        impressions = from_union([from_int, from_none], obj.get("impressions"))
        return KddiAdvertiserReportsResponseElement(enabledDisabledOn, id, createdOn, createdById, modifiedOn, modifiedById, disabled, reportDate, propertyId, mediaChannel, clicks, avgCPC, spend, bookings, totalBookings, rn, totalRN, revenue, totalRevenue, gre, totalGRE, koddiFileId, status, impressions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabledDisabledOn"] = from_none(self.enabledDisabledOn)
        result["id"] = from_union([from_str, from_none], self.id)
        result["createdOn"] = from_union([lambda x: from_list(to_float, x), from_none], self.createdOn)
        result["createdById"] = from_union([from_int, from_none], self.createdById)
        result["modifiedOn"] = from_union([lambda x: from_list(to_float, x), from_none], self.modifiedOn)
        result["modifiedById"] = from_union([from_int, from_none], self.modifiedById)
        result["disabled"] = from_union([from_bool, from_none], self.disabled)
        result["reportDate"] = from_union([lambda x: from_list(to_float, x), from_none], self.reportDate)
        result["propertyId"] = from_union([from_int, from_none], self.propertyId)
        result["mediaChannel"] = from_union([from_str, from_none], self.mediaChannel)
        result["clicks"] = from_union([from_int, from_none], self.clicks)
        result["avgCPC"] = from_union([from_str, from_none], self.avgCPC)
        result["spend"] = from_union([from_str, from_none], self.spend)
        result["bookings"] = from_union([from_int, from_none], self.bookings)
        result["totalBookings"] = from_union([from_int, from_none], self.totalBookings)
        result["rn"] = from_union([from_int, from_none], self.rn)
        result["totalRN"] = from_union([from_int, from_none], self.totalRN)
        result["revenue"] = from_union([from_str, from_none], self.revenue)
        result["totalRevenue"] = from_union([from_str, from_none], self.totalRevenue)
        result["gre"] = from_union([from_str, from_none], self.gre)
        result["totalGRE"] = from_union([from_str, from_none], self.totalGRE)
        result["koddiFileId"] = from_union([from_str, from_none], self.koddiFileId)
        result["status"] = from_union([from_int, from_none], self.status)
        result["impressions"] = from_union([from_int, from_none], self.impressions)
        return result


def KddiAdvertiserReportsResponsefromdict(s: Any) -> List[KddiAdvertiserReportsResponseElement]:
    return from_list(KddiAdvertiserReportsResponseElement.from_dict, s)


def KddiAdvertiserReportsResponsetodict(x: List[KddiAdvertiserReportsResponseElement]) -> Any:
    return from_list(lambda x: to_class(KddiAdvertiserReportsResponseElement, x), x)
