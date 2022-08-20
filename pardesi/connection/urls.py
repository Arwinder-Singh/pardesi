
# from django import views
from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='index'),
     path('login/',views.login,name='login'),
     path('signup/',views.signup,name='signup'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('logout',views.logout,name='logout'),
     path('addRoom',views.addRoom,name='addRoom'),
     path('roomDetails/<str:through>/<str:pk>/',views.roomDetails,name='roomDetails'),
     path('rooms',views.rooms,name='rooms'),
     
     
     ]