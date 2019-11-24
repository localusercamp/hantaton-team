from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in),
    path('login/auth/', views.authenticate),
    # path('admin/', admin.site.urls),
    # path('register/', views.register, name='register'),
    # path('user_login/', views.user_login, name='user_login'),
    # path('admin/', admin.site.urls),
    # path('',views.index,name='index'),
    # path('special/',views.special,name='special'),
    # path('logout/', views.user_logout, name='logout')
]