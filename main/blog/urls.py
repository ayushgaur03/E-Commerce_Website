from django.urls import path,include
from . import views 

urlpatterns = [
    path("",views.index, name='BlogHome'),
    path("blogpost/blog<int:bid>",views.blogpost, name='BlogPost'),
]