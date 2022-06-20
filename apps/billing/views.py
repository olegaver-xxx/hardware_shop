from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment


class PaymentView(DetailView, LoginRequiredMixin):
    template_name = 'payment.html'
    model = Payment
    context_object_name = 'payment'
