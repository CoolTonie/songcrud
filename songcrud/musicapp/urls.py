from re import L
from django.urls import path, include
from .views import ArtisteView, LyricView
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'',ArtisteView)
router.register(r'',LyricView)

urlpatterns= [
    path('',include(router.urls))
]