from django.db import models
from mongoengine import fields, Document


class Employee(Document):
    id = fields.ObjectId()
    name = fields.StringField(required=True)


class KoddiFiles(Document):
    id = fields.ObjectId()
    originalFileName = fields.StringField(db_field='OriginalFileName')
    uploadedFileName = fields.StringField(db_field='UploadedFileName')
    fileType = fields.IntField(db_field='FileType')
    fileOcrStatus = fields.IntField(db_field='FileOcrStatus')
    brandType = fields.IntField(db_field='BrandType')
    startDate = fields.DateTimeField(db_field='StartDate')
    endDate = fields.DateTimeField(db_field='EndDate')
    enterpriseId = fields.IntField(db_field='EnterpriseId')
    propertyId = fields.IntField(db_field='PropertyId')
    notes = fields.StringField(db_field='Notes')
    bucketName = fields.StringField(db_field='BucketName')
    isCompleted = fields.BooleanField(db_field='IsCompleted')
    jobId = fields.StringField(db_field='JobId')
    createdById = fields.IntField(db_field='CreatedById')
    modifiedOn = fields.ListField(db_field='ModifiedOn')
    disabled = fields.BooleanField(db_field='Disabled')
    enabledDisabledOn = fields.StringField(db_field='EnabledDisabledOn')
    createdOn = fields.ListField(db_field='CreatedOn')
    modifiedById = fields.IntField(db_field='ModifiedById')

    meta = {'collection': 'koddifiles'}
