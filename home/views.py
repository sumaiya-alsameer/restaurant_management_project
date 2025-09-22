from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer



# Create your views here.


class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

