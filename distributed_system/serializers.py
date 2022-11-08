from rest_framework.serializers import ModelSerializer
from .models import Bank,Transaction


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'