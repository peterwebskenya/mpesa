from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name= 'hello' ),
    path('hi/', views.hi, name= 'hi'),
    path('evenodd/', views.evenodd, name= 'evenodd'),
    path('', views.error, name= 'error'),
    path('index/', views.index, name= 'index'),
    path('tables/', views.tables, name= 'tables'),
    path('variables/', views.variables, name= 'variables', ),
    path('var/', views.var, name= 'var'),
    path('emp/', views.emp, name= 'emp'),
    path('img/', views.img, name= 'OMG'),
    path('background/', views.background, name= 'Background'),
    path('image/', views.image, name= 'image'),
    path('session/', views.setsession, ),
    path('gsession',  views.getsession,),
    path('form/', views.form, ),






)
