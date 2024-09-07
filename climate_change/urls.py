from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.IndexPageView.as_view(), name='index_page'),
    path('elements/', views.ElementsPageView.as_view(), name='elements_page'),
    path('generic/', views.GenericPageView.as_view(), name='generic_page'),
    path('documentation/', views.GenericPageView.as_view(), name='documentation'),
    path('predict_climate/', views.predict_climate, name='predict_climate'),
    path('predict_climate_graphs/', views.predict_climate_graphs, name='predict_climate_graphs'),
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # Other URL patterns


]