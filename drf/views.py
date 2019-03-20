from django.shortcuts import render
from .serialize import TestModelSerialize, TestModelSerializeAll
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TestModel

token='asdfhgyerityoertp'

def drf_form(request):
    return render(request, 'drf/drf_form.html',{})


@api_view(["GET"])
def item_all(request):
    data = request.GET.get('token')
    if data == token:
        pass
    test = TestModel.objects.all()
    serializer = TestModelSerialize(test,
                                many=True,
                                context={'request':request},)
    return Response(serializer.data)
    data = {"error": True,"errors": 'No token',}
    return Response(data)

#только для просмотра, если необходим после просмотра данные менять
#лучше использовать реализацию функции item_update
#и передавать данный с методом PUT
@api_view(["GET"])
def item_detail(request,id):
    try:
        test = TestModel.objects.get(id=id)
    except:
        return Response({'error':True})
    serializer = TestModelSerialize(test,context={'request':request},)
    return Response(serializer.data)

@api_view(["POST"])
def item_create(request):
    serializer = TestModelSerialize(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        data = {
          "error": True,
          "errors": serializer.errors,
        }
        return Response(data)

@api_view(["GET", "PUT"])
def item_update(request,id):
    try:
        test = TestModel.objects.get(id=id)
    except:
        return Response({'error':True, 'errors':True})
    if request.method == "PUT":
        print(request.data)
        #для частичного обновления partial=True
        serializer = TestModelSerialize(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors, "errors": True,})
    serializer = TestModelSerialize(test)
    return Response(serializer.data)

@api_view(["GET"])
def item_delete(request,id):
    try:
        test = TestModel.objects.get(id=id)
    except:
        return Response({'error':True, 'errors':True})
    test.delete()
    return Response({"message": "Deleted"})
