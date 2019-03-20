from django.shortcuts import render, HttpResponse, Http404
from profiles.models import City, Country
import json
from itertools import groupby
from django.db.models import Count, F, Prefetch
from .forms import CountryForm
from django.http import JsonResponse
from django.forms.utils import flatatt
from load.models import NewCity, NewCountry


def add_js(request):
    # data = [[country,[city for city in City.objects.filter(country=id).values_list('name', flat=True)] ]
            # for country,id in Country.objects.values_list('country', 'id')]

    # qs = City.objects.all()
    # co = Country.objects.prefetch_related(Prefetch('city_set', queryset=qs, to_attr='all_city'))
    # data = [(str(item), list(map(str,item.all_city))) for item in co]

    qs = NewCity.objects.all()
    co = NewCountry.objects.prefetch_related(Prefetch('country_city', queryset=qs, to_attr='all_city'))
    data = [(str(item), list(map(str,item.all_city))) for item in co]


    data = json.dumps(data)
    return render(request, 'addjs/addjs.html',{'data':data})


def ajax_js(request):
    data = CountryForm()
    if request.is_ajax() and request.method == 'POST':
        print('AJAX')
        srv={}
        info = request.POST.get('country')
        try:
            a = NewCity.objects.filter(country=info)[:1000].values_list('city_name','id')
        except:
            return HttpResponse(reason="Error!!!!", status=203)
        else:
            srv['data'] = tuple(a)
            return JsonResponse(srv, content_type='application/json')

    elif request.method == "POST":
        print("POST")
        data = CountryForm(request.POST)
        srv = {}
        if data.is_valid():
            country = data.cleaned_data['country']
            city = data.cleaned_data['city']
            srv['country'] = country
            srv['city'] = city
            return render(request, 'addjs/result.html', {'data':srv})
    return render(request,'addjs/ajaxjs.html',{'data':data})
