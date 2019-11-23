from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .serializers import *
from .views import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
import json, io
from rest_framework.renderers import JSONRenderer

def ChooseLoginRole(request):
    return render(request, 'uber/index.html')

def StudentLogin(request):
    return render(request, 'uber/requestin.html')

def CompanyLogin(request):
    return render(request, 'uber/requestin.html')

def UniversityLogin(request):
    return render(request, 'uber/requestin.html')

def MentorLogin(request):
    return render(request, 'uber/requestin.html')



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
    # diction = {}
    # diction['username'] = 'newuser'
    # diction['first_name'] = 'Евгений'
    # diction['last_name'] = 'Полозов'
    # diction['third_name'] = 'Дмитриевич'
    # diction['password'] = 'password'
    CustomUserSerializer.create(CustomUserSerializer, diction)
@csrf_exempt
def CreateUniversity(request):
    # diction = {}
    # diction['username'] = 'newuser'
    # diction['first_name'] = 'Евгений'
    # diction['last_name'] = 'Полозов'
    # diction['third_name'] = 'Дмитриевич'
    # diction['password'] = 'password'
    CustomUserSerializer.create(CustomUserSerializer, diction)

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
    # diction = {}
    # diction['username'] = 'newuser'
    # diction['first_name'] = 'Евгений'
    # diction['last_name'] = 'Полозов'
    # diction['third_name'] = 'Дмитриевич'
    # diction['password'] = 'password'
    CustomUserSerializer.create(CustomUserSerializer, diction)
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