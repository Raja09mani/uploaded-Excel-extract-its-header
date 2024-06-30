# myapp/urls.py
from django.urls import path
from xlsupextApp.views import update_database

urlpatterns = [
    path('update_database/', update_database, name='update_database'),
]
