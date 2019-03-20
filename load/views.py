from django.shortcuts import render, HttpResponse, Http404
from .forms import LoadFile
from profiles.models import Country, City
from .models import NewCountry, NewCity

from django.db.models.aggregates import Count
from django.db.models import Q





def load_country(request):
    form = LoadFile()
    if request.method == "POST":
        form = LoadFile(request.POST,files=request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            text = [item.decode('utf-8').strip().split()[0]
                    for item in file.readlines()]
            Country.objects.all().delete()
            for item in text:
                Country.objects.create(country=item)
            text = Country.objects.values_list('country', flat=True)

            return render(request, "load/succes.html",
                          {'text':text})
    return render(request, "load/country.html",
                  {"form_c":form})

def load_city(request):
    form = LoadFile()
    if request.method == "POST":
        form = LoadFile(request.POST,files=request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            import pandas as pd
            xs = pd.ExcelFile(file)
            sn = xs.sheet_names
            info = xs.parse(sheet_name=sn[0])
            country = info['country'].to_list()
            city = info['city'].to_list()
            City.objects.all().delete()
            bad_info={}
            for c,t in zip(country,city):
                # if Country.objects.filter(country=c.strip()).exists():
                try:
                    a = Country.objects.get(country=c.strip())
                except:
                    bad_info[c]=t

                else:
                    for name in t.split(','):
                        City.objects.create(country=a,name=name.strip())
            info = City.objects.all()

            return render(request,'load/succes.html', {'text':info,
                                                       'bad_info':bad_info})
    return render(request, "load/city.html",{'form_c':form})


def load_country_csv(request):
    form = LoadFile()
    if request.method == "POST":
        form = LoadFile(request.POST,files=request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            import pandas as pd
            info = pd.read_csv(file, sep=',',encoding='utf-8',usecols=['country_id','title_ru'])
            NewCountry.objects.all().delete()
            lst = [ NewCountry(id,name) for id, name in zip(info['country_id'],info['title_ru'])]
            NewCountry.objects.bulk_create(lst)

            info = NewCountry.objects.all()
            return render(request,'load/succes.html', {'text':info})
    return render(request, "load/country.html",
                  {"form_c":form})


def load_city_new(request):
    # NewCity.objects.all().delete()
    import pandas as pd
    file = 'C:/Users/asdim/Desktop/ForAppDjango/CSV/_cities.csv'
    # # 2246812
    info = pd.read_csv(file, sep=',',encoding='utf-8', usecols=['country_id','title_ru'])
    info = info[info['country_id']==1]

    с = NewCountry.objects.get(id=1)
    info = [NewCity(country=с,city_name=name) for id,name in zip(info['country_id'], info['title_ru'])]
    NewCity.objects.bulk_create(info)

    info = NewCity.objects.values_list('city_name', flat=True)
    length = info.count()

    return render(request,'load/succes.html', {'text':info,
                                               'length':length})
from django.db.models.aggregates import Count
from django.db.models import Q
def duplicate(request):
    info = NewCity.objects.values(
        'city_name')\
    .annotate(count_city=Count('city_name'))\
    .filter(Q(country=2),Q(count_city__gt=1))

    length = info.count()
    return render(request, 'load/succes.html', {'text':info,
                                                'length':length})
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
def unique_city(request):
    u_all = NewCity.objects.values(
        'city_name')\
    .annotate(count_city=Count('city_name'))\
    .filter(Q(country=2),~Q(count_city__exact=0)).order_by('-count_city', 'city_name')
    length = u_all.count()

    page = request.GET.get('page')
    paginator = Paginator(u_all,10)
    try:
        info = paginator.page(page)
    except PageNotAnInteger:
        info = paginator.page(1)
    except EmptyPage:
        info = paginator.page(paginator.num_pages)
    return render(request, 'load/succes.html', {'info':info,
                                                'page':page,
                                                    'length':length})

def test_sql_join():
    NewCountry.objects.select_related().values_list(
        'country_city__city_name','country_name')
    NewCity.objects.select_related('country').values_list(
        'country__country_name', 'city_name')
    Country.objects.select_related().values_list('city__name', 'country')
