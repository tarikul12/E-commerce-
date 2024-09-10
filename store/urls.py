from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("store/", views.store, name="store"),
    path("category/<slug:category_slug>/", views.store, name="products_by_category"),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path("submit_review/<int:product_id>", views.submit_review, name="submit_review"),
    
]

