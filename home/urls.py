from django.urls import path
from .views import *

urlpatterns = [
   path('menu-categories/', MenuCategoryListAPIView.as_view(), name='menu-categories'), 
]