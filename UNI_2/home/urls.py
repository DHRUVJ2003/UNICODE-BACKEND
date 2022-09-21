from django.urls import path
from . import views

urlpatterns = [
    path('dhruv/<int:a>/<int:b>/',views.tp,name='request')    
]
