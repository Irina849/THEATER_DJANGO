from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Poster
from django.db.models import Q
from datetime import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class NextE(ListView):
    model = Poster
    template_name = template_name = 'next_events.html'
    now = datetime.now()
    queryset = Poster.objects.filter(performace_date__gte = now).all()


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
    	return render(request, 'myapp/login_error.html')
        