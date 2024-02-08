from rest_framework import serializers
from next.models import Gmail


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gmail
        fields = ('email', 'password')
