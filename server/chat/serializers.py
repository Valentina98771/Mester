from rest_framework import serializers
from chat.models import PrivateMessage
from django.contrib.auth import get_user_model
User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = PrivateMessage
        fields = ['sender', 'receiver', 'message', 'timestamp']
