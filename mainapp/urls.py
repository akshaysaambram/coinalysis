from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('coins/', views.coins, name='coins'),
    path('coins/<str:pk>/', views.coin, name='coin'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('transactions/', views.transactions, name='transactions'),
    path('analysis/<str:pk>/', views.analysis, name='analysis'),

    path('', include('users.urls')),
]