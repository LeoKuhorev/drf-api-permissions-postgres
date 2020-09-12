from django.urls import path

from api_v1.items.views import ItemList, ItemDetail

urlpatterns = [
    path('<int:pk>/', ItemDetail.as_view(), name='api-items-detail'),
    path('', ItemList.as_view(), name='api-items-list'),
]
