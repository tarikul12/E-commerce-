from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("forgetPassword/", views.forgetPassword, name="forgetPassword"),
    
    path("chatbot/", views.my_orders, name="chatbot"),
    path("response/", views.my_orders, name="response"),
    path("my_orders/", views.my_orders, name="my_orders"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path("change_password/", views.change_password, name="change_password"),
    path("order_detail/<int:order_id>", views.order_detail, name="order_detail"),
]
