from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import/nasdaq-index', views.import_nasdaq_index, name='import_nasdaq_index'),
    path('import/weight-classes', views.import_weight_classes, name='import_weight_classes'),
    path('import/', views.import_data, name='importer'),
    path('laboratory/', views.laboratory, name='laboratory'),
]