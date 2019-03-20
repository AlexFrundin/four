from django.shortcuts import render
from .models import Human

def home(request):
    context = {}
    qs = Human.objects.filter(age__gt=17)
    qs = qs.order_by('name')
    context['humans'] = qs
    return render(request, 'index.html',context)

def detail(request,pk):
    context = {}
    context['human'] = Human.objects.get(pk=pk)
    return render(request, 'detail__.html', context)
