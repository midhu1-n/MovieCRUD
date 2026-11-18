from rest_framework import serializers
from Expense.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"
        read_only_fields=['id','created','updated','user']