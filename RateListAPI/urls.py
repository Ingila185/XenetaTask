from django.urls import path
from . import views

urlpatterns = [
    path('rates/', views.RateList.as_view())
]