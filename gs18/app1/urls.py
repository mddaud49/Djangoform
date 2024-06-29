from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.ShowData),
    path('suc/',views.Success),

]