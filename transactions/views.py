from django.shortcuts import render

from transactions.models import Payment

# Create your views here.

def payment_history(request):
    transactions = None
    if request.user.is_authenticated:
         transactions = Payment.objects.filter(user = request.user).order_by('-pk')
    context = {"transactions":transactions}
    template = "payments.html"
    return render(request,template,context)
