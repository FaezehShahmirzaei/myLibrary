from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_users),
    # path('userbooks/', views.userbooks),
    path('<str:username>/',views.userinfo ,name='username'),

]
