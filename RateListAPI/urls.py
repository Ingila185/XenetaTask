from django.urls import path
from . import views

urlpatterns = [
    #path('', views.rates)
    path('', views.RateList.as_view())
]