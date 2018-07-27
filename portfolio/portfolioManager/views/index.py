from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolioManager.models import UserPortfolio, Stocks
from django.contrib.messages import get_messages
from portfolioManager.forms import stock_forms

class IndexView(LoginRequiredMixin, View):
    """
    This renders the home page of the user.
    """
    def get(self, request):
        storage = get_messages(request)
        error_message = None
        for message in storage:
            error_message = message
        user_portfolio = UserPortfolio.objects.filter(user_id=request.user.id)
        context = {'user_portfolio': user_portfolio,
                   'error_message': error_message,
                   'add_stock_form': stock_forms.AddStockForm()}
        return render(request, 'portfolioManager/index.html', context)