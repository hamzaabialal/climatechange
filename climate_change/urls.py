from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('elements/', views.ElementsPageView.as_view(), name='elements_page'),
    path('generic/', views.GenericPageView.as_view(), name='generic_page'),
    path('documentation/', views.GenericPageView.as_view(), name='documentation'),

]