from django.urls import path
from . import views

urlpatterns = [
    path('', views.access_keys_list, name='home'),
    path('new-key/', views.request_access_key, name='new_key')
]
