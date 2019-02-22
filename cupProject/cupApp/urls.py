from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('hello/<str:name>/', views.hello, name = 'Greeting'),
    path('times2/<int:number>/', views.timesTwo, name = 'Double'),
    path('total/<int:number>/', views.total, name = 'Totality'),
    path('newcup/',views.newCup, name = 'newCup'),
    path('allcup/',views.cupView, name = 'viewCup'),
    path('cupdate/', views.updateCup, name = 'updateCups'),
    path('display/' , views.cupIndex , name = 'ListofCups'),
]