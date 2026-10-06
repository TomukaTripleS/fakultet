from datetime import date

from django.shortcuts import render

from .models import ExchangeProgram


def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    return render(
        request,
        "exchange/exchange_list.html",
        {"programs": programs, "today": date.today()},
    )
