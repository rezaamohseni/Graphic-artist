from django.urls import path , include
from .views import *

app_name = 'root'
urlpatterns = [
    path('', HomeView.as_view() , name = 'home'),
    path('service/', Service.as_view() , name = 'service'),
]
