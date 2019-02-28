from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioPost
from django.http import HttpResponseRedirect

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.order_by('-id')
    return render(request, 'portfolio.html', {'portfolios' : portfolios})

def portfoliopost(request):
    if request.method == 'POST' :
        form = PortfolioPost(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit = False)
            post.save()
            return HttpResponseRedirect('/portfolio/')
    else:
        form = PortfolioPost()
        return render(request, 'newphoto.html', {'form' : form})
