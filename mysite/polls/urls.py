from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
]

''' 'service': 'pg_service',
    'passfile': 'pgpass','''