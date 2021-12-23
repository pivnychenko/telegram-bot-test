from django.urls import path
from . import views

urlpatterns = [
    path('get_hook/', views.get_hook, name="get_hook"),
    path('set-hook/', views.set_hook, name="set_hook"),
]
