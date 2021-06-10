from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views
urlpatterns = [
    path('forma', views.forma, name = 'forma'),
    path('',views.forma, name = 'index'),
    path('submit',views.submit, name = 'submit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('list', views.list, name='list'),
    path('sortdata', views.sortdata, name='sortdata'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update')

]
