from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name='image_gallery'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='image_gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('image_gallery:home')), name='logout'),
    path('image/create/', views.ImageCreateView.as_view(), name='image_create'),
    path('image/update/<int:pk>', views.ImageUpdateView.as_view(), name='image_update'),
    path('image/detail/<int:pk>', views.ImageDetailView.as_view(), name='image_detail'),
    path('image/delete/<int:pk>', views.ImageDestroyView.as_view(), name='image_delete'),

    path('catagory/create/', views.CatagoryCreateAPIView.as_view(), name='catagory_create'),

    path('user/create/', views.UserCreateView.as_view(), name='user_create'),

    path('payment/', TemplateView.as_view(template_name='image_gallery/payment.html'), name='payment'),
    
]   