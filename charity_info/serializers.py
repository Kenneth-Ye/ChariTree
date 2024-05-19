from rest_framework import serializers
from .models import Cause, User_transaction, Charity_transaction

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['id', 'is_approved', 'name', 'charity', 'wallet_addr', 'description']

class CharityTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity_transaction
        fields = ['id', 'create_date', 'sender', 'cause', 'amount']

class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_transaction
        fields = ['id', 'create_date', 'sender', 'charity', 'amount']
        

