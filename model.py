from mongoengine import *


class EndPoints(Document):
    total = IntField(required=True)
    ok = IntField(required=True)
    error = IntField(required=True)
    company = StringField(required=True)


class Card(Document):
    client_name = StringField(required=True)
    error_number = IntField(required=True)
    ip = StringField(required=True)
    company = StringField(required=True)


class Users(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    company = StringField(required=True)


class Checklist(Document):
    name = StringField(required=True)
    number = StringField(required=True)


class ClientChecks(Document):
    company = StringField(required=True)
    client_name = StringField(required=True)
    client_list = DictField(required=True)
