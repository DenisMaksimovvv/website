from django.urls import path

from .views import HomePageView, AboutPageView, ProductPageView, StorePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', AboutPageView.as_view(), name='about'),
    path('', ProductPageView.as_view(), name='products'),
    path('', StorePageView.as_view(), name='store'),
]