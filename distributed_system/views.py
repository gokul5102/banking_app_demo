from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from .models import Bank,Transaction
from .serializers import BankSerializer,TransactionSerializer
from rest_framework import status
from django.http import JsonResponse
from .tasks import test_func

# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")


@api_view(["GET"])
def checkBalance(request,id):
    # account_no=request.data.get('account_no')
    print(request.META['SERVER_PORT'])
    bal=Bank.objects.get(account_number=id)
    if(bal):
        ser = BankSerializer(bal)
        return JsonResponse(ser.data,status= status.HTTP_200_OK)
    else:
        return Response("No student found", status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def transfer(request):
    print("12",request.data)
    if request.data:
        sender = request.data.get('sender')
        receiver = request.data.get('receiver')
        amount = request.data.get('amount')
        s=Bank.objects.get(name=sender)
        r=Bank.objects.get(name=receiver)
        s.balance-=amount
        r.balance+=amount
        s.save()
        r.save()
        t=Transaction.objects.create(sender=sender,receiver=receiver,amount=amount)
        qs=Transaction.objects.all()
        if(qs.count()==1):
            for a in qs:
                a.save(using="second_db")
            Transaction.objects.all().delete()
        return Response("Done", status=status.HTTP_200_OK)

