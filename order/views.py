from django.shortcuts import render
from .models import Order
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import OrderSerializer


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all(),
    serializer_class = OrderSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdate(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@csrf_exempt
def OrderlistRest(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def OrderDetails(request, smbdOrderID):
    try:
        order = Order.objects.get(smbdOrderID=smbdOrderID)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
