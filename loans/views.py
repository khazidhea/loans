from django.views.generic import ListView, CreateView
from django.shortcuts import render

from .models import Loan


class LoanListView(ListView):
    model = Loan


class LoanCreateView(CreateView):
    model = Loan
    fields = ['amount']
    success_url = '/'
