from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .serializers import *
from .views import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
import json, io
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect

def ChooseLoginRole(request):
    return render(request, 'uber/index.html')

def StudentLogin(request):
    return render(request, 'uber/requestin.html')

def CompanyLogin(request):
    return render(request, 'uber/logInCompany.html')

def UniversityLogin(request):
    return render(request, 'uber/requestin.html')

def MentorLogin(request):
    return render(request, 'uber/requestin.html')


def CreateProjectView(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'uber/createprojectview.html')
    else:
        return HttpResponseBadRequest()

def CreateProject(request):
    pass


def ChooseRegisterRole(request):
    return render(request, 'uber/chooseregrole.html')

def StudentRegister(request):
    return render(request, 'uber/regnewuserS.html')

def MentorRegister(request):
    return render(request, 'uber/regnewuserM.html')

def CompanyRegister(request):
    return render(request, 'uber/regnewuserC.html')

def UniversityRegister(request):
    return render(request, 'uber/regnewuserU.html')


# start - создание обьектов юзера + обьекта по роли
@csrf_exempt
def CreateCompany(request):
    to_custom_user = {
        'email':request.POST.get('email'),
        'password':request.POST.get('password'),
        'username':request.POST.get('inn'),
        'inn':request.POST.get('inn'),
        'role':'company',
    }
    to_company = {
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        'phone':request.POST.get('phone'),
        'orgn':request.POST.get('orgn'),
        'username':request.POST.get('inn'),
        'kpp':request.POST.get('kpp'),
        'bank':request.POST.get('bank'),
        'director':request.POST.get('director'),
        'bik':request.POST.get('bik'),
        'city':request.POST.get('city'),
    }
    CustomUserSerializer.create(CustomUserSerializer, to_custom_user, to_company)

@csrf_exempt
def CreateUniversity(request):
    to_custom_user = {
        'email':request.POST.get('email'),
        'password':request.POST.get('password'),
        'username':request.POST.get('username'),
        'inn':request.POST.get('inn'),
        'role':'university',
    }
    to_university = {
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        'phone':request.POST.get('phone'),
        'orgn':request.POST.get('orgn'),
        'inn':request.POST.get('inn'),
        'kpp':request.POST.get('kpp'),
        'bank':request.POST.get('bank'),
        'director':request.POST.get('director'),
        'bik':request.POST.get('bik'),
        'city':request.POST.get('city'),
    }
    CustomUserSerializer.create(CustomUserSerializer, to_custom_user, to_university)

@csrf_exempt
def CreateStudent(request):
    # ВЫВЕСТИ В СЕЛЕКТОР ВО ФРОНТЕ ОБЬЕКТ И В СКОБКАХ ЕГО ИД ЧТОБЫ ЗАПАРСИТЬ С ФРОНТА ИД ИЗ СТРОКИ СЮДА
    to_custom_user = {
        'email':request.POST.get('email'),
        'password':request.POST.get('password'),
        'username':request.POST.get('username'),
        'role':'student',
    }
    to_student = {
        'university_id':request.POST.get('university_id'),
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        'phone':request.POST.get('phone'),
    }
    CustomUserSerializer.create(CustomUserSerializer, to_custom_user, to_student)

@csrf_exempt
def CreateMentor(request):
    # ВЫВЕСТИ В СЕЛЕКТОР ВО ФРОНТЕ ОБЬЕКТ И В СКОБКАХ ЕГО ИД ЧТОБЫ ЗАПАРСИТЬ С ФРОНТА ИД ИЗ СТРОКИ СЮДА
    to_custom_user = {
        'email':request.POST.get('email'),
        'password':request.POST.get('password'),
        'username':request.POST.get('username'),
        'role':'mentor',
    }
    to_mentor = {
        'university_id':request.POST.get('university_id'),
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        'phone':request.POST.get('phone'),
    }
    CustomUserSerializer.create(CustomUserSerializer, to_custom_user, to_mentor)
# end - создание обьектов юзера + обьекта по роли

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SignUpViewCompanyUniversity(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SignUpViewStudentMentor(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'