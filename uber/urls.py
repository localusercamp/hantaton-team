from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import SignUpView, SignUpViewStudentMentor, SignUpViewCompanyUniversity
from . import views
from django.shortcuts import render

urlpatterns = [
    path('chooseregrole/', views.ChooseRegisterRole), # перейти в выбор роли для регистраици
    path('chooseregrole/regnewuserC/', views.CompanyRegister), # компания
    path('chooseregrole/regnewuserU/', views.UniversityRegister), # универ
    path('chooseregrole/regnewuserS/', views.StudentRegister), # студент
    path('chooseregrole/regnewuserM/', views.MentorRegister), # ментор
    path('chooseregrole/regnewuserC/create/', views.CreateCompany), # (запрос) создать компанию
    path('chooseregrole/regnewuserU/create/', views.CreateUniversity), # (запрос) создать универ
    path('chooseregrole/regnewuserS/create/', views.CreateStudent), # (запрос) создать студент
    path('chooseregrole/regnewuserM/create/', views.CreateMentor), # (запрос) создать ментор




    path('chooseloginrole/', views.ChooseRegisterRole),
    path('loginC/', views.CompanyLogin), # компания
    path('loginU/', views.UniversityLogin), # универ
    path('loginS/', views.StudentLogin), # студент
    path('loginM/', views.MentorLogin), # ментор

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('uber/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signupstudent/', SignUpViewStudentMentor.as_view(), name='signup'),
    path('signupmentor/', SignUpViewStudentMentor.as_view(), name='signup'),
    path('signupcompany/', SignUpViewCompanyUniversity.as_view(), name='signup'),
    path('signupuniversity/', SignUpViewCompanyUniversity.as_view(), name='signup'),
]