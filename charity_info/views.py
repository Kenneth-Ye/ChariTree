from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Cause, User_transaction, Charity_transaction
from .serializers import CauseSerializer, UserTransactionSerializer, CharityTransactionSerializer
from custom_auth.serializers import AccountSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

###
@api_view(['POST'])
def add_cause(request):
    is_approved = request.data['is_approved']
    name = request.data['cause_name']
    charity_name = request.data['charity_name']
    charity_user = User.objects.get(username=charity_name)
    wallet_addr = request.data['wallet_addr']
    description = request.data['cause_desc']
    cause = Cause(is_approved=is_approved, name=name, charity=charity_user,wallet_addr=wallet_addr,description=description)
    cause.save()
    serializer = CauseSerializer(cause, many=False) 
    return Response({'new cause': serializer.data}, status=200) 

###
@api_view(['GET'])
def get_causes(request):
    charity_name = request.query_params.get('charity_name')
    charity_user = User.objects.get(username=charity_name) 
    causes = charity_user.causes.all() 
    serializer = CauseSerializer(causes, many=True) 
    print(serializer.data)
    return Response({'causes': serializer.data}, status=200) 

###
@api_view(['GET'])
def get_transactions(request):
    username = request.data['username']
    user = User.objects.get(username=username) 
    transactions = user.sent_transactions.all() 
    serializer = UserTransactionSerializer(transactions, many=True) 
    return Response({"transactions": serializer.data}, status=200) 

###
@api_view(['POST'])
def post_transactions(request):
    username = request.data['username']
    user = User.objects.get(username=username)
    charity_name = request.data['charity_name']
    charity = User.objects.get(username=charity_name)
    amount = request.data['amount']
    
    user_trans = User_transaction(sender=user, charity=charity, amount=amount)
    user_trans.save()
    return Response({'user': username, 'charity': charity_name, 'amount': amount}, status=200)

###
@api_view(['GET'])
def get_charity_info(request):
    charity_name = request.query_params.get('charity_name')
    value = User.objects.filter(username=charity_name).aggregate(Sum("received_transactions__amount"))
    if value["received_transactions__amount__sum"] == None:
        return Response({'value': 0}, status=200)
    # back in website, call the get_transactions for the other rendering portion lmao
    return Response({'value': value["received_transactions__amount__sum"]}, status=200)

###
@api_view(['GET'])
def get_char_transactions(request):
    charity_name = request.query_params.get('charity_name')
    charity = User.objects.get(username=charity_name) 
    transactions = charity.charity_sent_transactions.all() 
    serializer = CharityTransactionSerializer(transactions, many=True) 
    return Response({'transactions': serializer.data}, status=200) 

###
@api_view(['POST'])
def post_char_transactions(request):
    charity_name = request.data['charity_name']
    charity = User.objects.get(username=charity_name)
    cause_name = request.data['cause_name']
    cause = Cause.objects.get(name=cause_name)
    amount = request.data['amount']
    
    charity_trans = Charity_transaction(sender=charity, cause=cause, amount=amount)
    charity_trans.save()
    # not sure if this is right
    serializer = CharityTransactionSerializer(charity_trans, many=False) 
    return Response({'new transaction': serializer.data}, status=200) 

### new below
@api_view(['GET'])
def get_user_data(request):
    user_id = request.data['user_id']
    name = User.objects.get(id=user_id).username
    address = User.objects.get(id=user_id).wallet_addr
    return Response({'username': name, 'wallet_addr': address}, status=200)

@api_view(['GET'])
def get_all_charities(request):
    charities = User.objects.filter(is_charity=True)
    serializer = AccountSerializer(charities, many=True)
    return Response({'charities': serializer.data}, status=200)

@api_view(['GET'])
def get_char_metadata(request):
    charity_name = request.query_params.get('charity_name')
    charity = User.objects.get(username=charity_name)
    serializer = AccountSerializer(charity)
    return Response({'info': serializer.data}, status=200)

@api_view(['GET'])
def pull_cause(request):
    cause_id= request.query_params.get('cause_id')
    cause = Cause.objects.get(id=cause_id)
    serializer = CauseSerializer(cause)
    return Response({'cause': serializer.data}, status=200)
    