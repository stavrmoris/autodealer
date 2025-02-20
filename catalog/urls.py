from django.urls import path
from . import views

urlpatterns = [
    # Главные страницы для каждой страны
    path('japanese/', views.japanese_main, name='japanese_main'),
    path('chinese/', views.chinese_main, name='chinese_main'),
    path('korean/', views.korean_main, name='korean_main'),

    # Каталоги для каждой страны
    path('japanese/catalog/', views.japanese_catalog, name='japanese_catalog'),
    path('chinese/catalog/', views.chinese_catalog, name='chinese_catalog'),
    path('korean/catalog/', views.korean_catalog, name='korean_catalog'),

    # Общие маршруты
    path('', views.chinese_main, name='chinese_main'),
    path('catalog/', views.car_list, name='car_list'),
    path('company/', views.company, name='company'),
    path('catalog/get-models', views.get_models, name='get_models'),
    path('japanese/catalog/filter-cars/', views.f1, name='filter_cars1'),
    path('chinese/catalog/filter-cars/', views.f2, name='filter_cars2'),
    path('korean/catalog/filter-cars/', views.f3, name='filter_cars3'),
    path('catalog/<int:car_id>/', views.car_detail, name='car_detail'),
]