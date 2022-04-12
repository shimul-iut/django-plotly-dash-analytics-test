from django.urls import include, path
from .views import OrderCreate, OrderList, OrderUpdate, OrderlistRest, OrderDetails

urlpatterns = [
    path('order/', OrderlistRest),
    path('order/<str:smbdOrderID>', OrderDetails),
    path('create/', OrderCreate.as_view(), name='create-order'),
    path('', OrderList.as_view()),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update-order')
]
