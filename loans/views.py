import json
from datetime import datetime

from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from .models import Loan


class LoanListView(ListView):
    model = Loan


class LoanCreateView(CreateView):
    model = Loan
    fields = ['amount']
    success_url = '/'


def api_day(request):
    result = {'today': datetime.today().strftime('%a')}
    return HttpResponse(json.dumps(result))
