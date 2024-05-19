from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'is_charity', 'wallet_addr', 'text_desc', 'subtitle']
        

