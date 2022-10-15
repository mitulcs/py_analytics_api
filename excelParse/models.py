from datetime import datetime
from email.policy import default
from django.db import models
from mongoengine import Document, fields
# Create your models here.


class MongoDocumentReports(Document):
    id = fields.ObjectId()
    monthid = fields.StringField(db_field='MonthID')
    managementcompany = fields.StringField(db_field='ManagementCompany')
    owner = fields.StringField(db_field='Owner')
    market = fields.StringField(db_field='Market')
    comparablestatus = fields.StringField(db_field='ComparableStatus')
    globalindicator = fields.StringField(db_field='GlobalIndicator')
    channel = fields.StringField(db_field='Channel')
    inncode = fields.StringField(db_field='InnCode')
    property = fields.StringField(db_field='Property')
    revenue = fields.LongField(db_field='Revenue')
    reservation = fields.LongField(db_field='Reservation')
    roomnights = fields.LongField(db_field='RoomNights')
    adr = fields.LongField(db_field='ADR')

    meta = {'collection': 'mongoTest'}


#   # createdOn = fields.ListField(db_field='CreatedOn')
#     # createdById = fields.IntField(db_field='CreatedById')
#     # modifiedOn = fields.ListField(db_field='ModifiedOn')
#     # modifiedById = fields.IntField(db_field='ModifiedById')
#     # disabled = fields.BooleanField(db_field='Disabled')
#     # enabledDisabledOn = fields.StringField(db_field='EnabledDisabledOn')


    # id = fields.ObjectId()
    # monthid = fields.StringField(db_field='MonthID')
    # managementcompany = fields.StringField(db_field='ManagementCompany')
    # owner = fields.StringField(db_field='Owner')
    # market = fields.StringField(db_field='Market')
    # comparablestatus = fields.StringField(db_field='ComparableStatus')
    # globalindicator = fields.StringField(db_field='GlobalIndicator')
    # channel = fields.StringField(db_field='Channel')
    # inncode = fields.StringField(db_field='InnCode')
    # property = fields.StringField(db_field='Property')
    # revenue = fields.LongField(db_field='Revenue')
    # reservation = fields.LongField(db_field='Reservation')
    # roomnights = fields.LongField(db_field='RoomNights')
    # adr = fields.LongField(db_field='ADR')