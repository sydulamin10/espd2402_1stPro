from django.urls import path
from .views import home, delete

urlpatterns = [
    path('', home, name='home'),
    path('delete/<id>/', delete, name='delete'),
]
