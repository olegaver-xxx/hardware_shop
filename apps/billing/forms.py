from django import forms
from .models import Payment, Order

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'product_list'