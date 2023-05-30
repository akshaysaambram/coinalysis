from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('coins/', views.coins, name='coins'),
    path('coins/<str:pk>/', views.coin, name='coin'),
    path('portfolio/', views.portfolio, name='portfolio'),
]