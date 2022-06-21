from django import forms
from .models import Payment, Order


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'