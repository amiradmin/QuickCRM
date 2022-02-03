from rest_framework import serializers
from django.contrib.auth.models import User
from training.models import Event,Category
from exam_certification.models import Exam
# class MessageListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     user = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     targetUser = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     readStatus = serializers.BooleanField()
#     created_at = serializers.DateTimeField()
#     userFullName = serializers.SerializerMethodField()
#     senderAvatarUrl = serializers.SerializerMethodField()
#
#
#     def get_userFullName(self, obj):
#         targetUser = obj.user.first_name + " " + obj.targetUser.last_name
#         return targetUser
#
#     def get_senderAvatarUrl(self, obj):
#         targetUser = "https://tempavatar.png"
#         return targetUser
#

class EventSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=512)

class ProductCatSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=512)
    description = serializers.CharField(required=False, allow_blank=True, max_length=4096)
    image = serializers.SerializerMethodField()


    def get_image(self, obj):
        print("Here")
        if obj.pic:
            return 'http://erp.tescan.ca' + obj.pic.url
        else:
            return None

class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    # category = serializers.CharField(required=False, allow_blank=True, max_length=512)
    name = serializers.CharField(required=False, allow_blank=True, max_length=512)
    code = serializers.CharField(required=False, allow_blank=True, max_length=512)
    price = serializers.CharField(required=False, allow_blank=True, max_length=512)
    type = serializers.CharField(required=False, allow_blank=True, max_length=512)
    description = serializers.CharField(required=False, allow_blank=True, max_length=4096)
    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_category(self, obj):
        category =ProductCatSerializer(obj.category).data
        return category

    def get_image(self, obj):
        print("Here")
        if obj.pic:
            return 'http://erp.tescan.ca' + obj.pic.url
        else:
            return None


class CategorySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=512)
    subCategory = serializers.SerializerMethodField()

    def get_subCategory(self, obj):
        subCategory = obj.form.all()
        subCatList=[]
        for item in subCategory:
            subCatList.append(item.name)
        return subCatList


class EventSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=512)
    start_date = serializers.DateTimeField()
    country = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()



    def get_country(self, obj):

        if obj.country:
            return obj.country.name


    def get_location(self, obj):
        return obj.location.name

    def get_category(self, obj):
        categories = obj.formCategory.all()
        return CategorySerializer(categories,many=True).data




class ExamSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=512)
    code = serializers.CharField(required=False, allow_blank=True, max_length=512)
    venue = serializers.CharField(required=False, allow_blank=True, max_length=512)
    sequence = serializers.CharField(required=False, allow_blank=True, max_length=512)
    invigilator = serializers.CharField(required=False, allow_blank=True, max_length=512)
    # country = serializers.SerializerMethodField()
    # location = serializers.SerializerMethodField()
    # category = serializers.SerializerMethodField()

    #
    # def get_country(self, obj):
    #
    #     if obj.country:
    #         return obj.country.name
    #
    #
    # def get_location(self, obj):
    #     return obj.location.name
    #
    # def get_category(self, obj):
    #     categories = obj.formCategory.all()
    #     return CategorySerializer(categories,many=True).data
