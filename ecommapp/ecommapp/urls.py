"""
URL configuration for ecommapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home_view'),
    path('register',views.RegisterView.as_view(),name='reg_view'),
    path('login',views.UserLoginView.as_view(),name='login_view'),
    path('logout',views.UserLogoutView.as_view(),name='logout_view'),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail_view'),
    path('carts/<int:id>',views.AddtoCartView.as_view(),name='cart_view'),
    path('carts/list',views.CartListView.as_view(),name='cartlist_view'),
    path('order/place/<int:cart_id>',views.PlaceOrderView.as_view(),name='order_view'),
    path('order/delete/<int:id>',views.OrderDeleteView.as_view(),name='delete_view'),
   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 











