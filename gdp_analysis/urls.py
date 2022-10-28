from django.urls import path
from .views import index,line

urlpatterns = [

    path('', index, name='index'),
    path('line/', line, name='line')

]