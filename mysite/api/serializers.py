from rest_framework import serializers
from django.contrib.auth.models import User
from training.models import Event

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



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

