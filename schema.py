import graphene
from graphene_mongo import MongoengineObjectType
from Models import User

class UserType(MongoengineObjectType):
    class Meta:
        model = User.User
        fields = ("_id" , "name" , "lastname")
