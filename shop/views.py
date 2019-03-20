from django.shortcuts import render, HttpResponse, redirect
from .models import Catalog,SubCatalog, Product
from .forms import MyForm, MyFormModels


def shop(request):
    catalogs = Catalog.objects.all()
    print(catalogs)
    subcatalogs = {}
    for catalog in catalogs:
        subcatalogs[catalog] = catalog.subcatalog_set.all()
    print(subcatalogs)
    return render(request, 'shop.html', {'sub':subcatalogs})


def get_form(request):
    context = {}
    context['my_form'] = MyForm()
    if request.method == 'POST':
        myform = MyForm(request.POST)
        if myform.is_valid():
            q = myform.cleaned_data.get('q')
            list_name = myform.cleaned_data['list_name']
            category_name = myform.cleaned_data['category_name']
            print(q)
            print(list_name)
            print(category_name)
            e  = Edit(q,list_name,category_name)
            e.save()
            return HttpResponse("Ok")

    #модифицировать файл my_form так чтобы отображалась вся инфа
    #которую пользователи отправляли

    return render(request, 'my_form.html', context)

def accept(request):
    return HttpResponse('Ok')



def get_form_st(request):
    context = {}
    # print(request.POST)
    if request.method == "POST":
        foo = {}
        foo['name'] = request.POST.get('name')
        foo['email'] = request.POST.get('email')
        foo['number'] = request.POST.get('number')
        foo['password'] = request.POST.get('password')
        # return redirect('accept_name', foo=foo)
        return render(request, 'accept.html', {'foo':foo})

    return render(request, 'my_form_standart.html', context)

def get_form_model(request):
    context={}
    context['form'] = MyFormModels()
    if request.method == "POST":
        form = MyFormModels(request.POST)
        form.save()
        context['form'] = form
    return render(request, 'model_form.html', context)
