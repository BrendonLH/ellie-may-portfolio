from django.urls import path

from .views import HomePageView, FactDetailView, FactListView

urlpatterns = [
    path("", HomePageView.as_view(), name='ellies_home'),
    path("facts", FactListView.as_view(), name='facts'),
    path('<int:pk>/', FactDetailView.as_view(), name='fact_detail'),
]
