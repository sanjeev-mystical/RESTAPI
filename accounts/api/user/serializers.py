import datetime
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from status.api.serializers import StatusInlineUserSerializer
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    #statuses = StatusInlineUserSerializer(source='status_set', many='True', read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
            #'statuses'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('detail', kwargs={'username': obj.username}, request=request)

    def get_status(self, obj):
        request = self.context.get('request')
        qs = obj.status_set.all().order_by('-timestamp')  # [:6]
        data = {
            'uri': self.get_uri(obj) + '/status/',
            'last': StatusInlineUserSerializer(qs.first(), context={'request': request}).data,
            'recent': StatusInlineUserSerializer(qs[:6], many=True, context={'request': request}).data

        }
        return data
