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
