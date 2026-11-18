from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=30)
    amount=models.IntegerField()
    category_choices=(('food','Food'),('health','Health'),('entertainment','Entertainment'),('shopping','Shopping'),('others','Others'))
    category=models.CharField(max_length=30,choices=category_choices)
    priorty_choices=(('need','Need'),('want','Want'))
    priorty=models.CharField(max_length=30,choices=priorty_choices)
    payment_choices=(('upi','UPI'),('cash','CASH'))
    payment_method=models.CharField(max_length=30,choices=payment_choices)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
