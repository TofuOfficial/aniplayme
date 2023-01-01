from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<str:anim>/<str:ep>/', views.show_ep, name='watch')
]