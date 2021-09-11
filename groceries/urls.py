from django.urls import path
from .views import GroceriesList, GroceriesDetail

urlpatterns = [
    path('', GroceriesList.as_view(), name='groceries_list'),
    path('<int:pk>/', GroceriesDetail.as_view(), name='groceries_detail'),
]
