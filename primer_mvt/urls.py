from django.contrib import admin
from django.urls import path
from family.views import create_family, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-family/', create_family, name='create_family'),
    path('list-family/', list_family, name='list_family')
]
