from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['name', 'discription', 'time', 'money']
    
    def create(self, data, _university, _company):
        project = Project(name=data['name'], discription=data['discription'], time=data['time'], money=data['money'], univresity=_university, company=_company)
        project.save()

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data, user):
        student = Student(name=data['name'], email=data['email'], phone=data['phone'], linked_user=user)
        student.save()

class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = ['name', 'email', 'phone', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data, user):
        mentor = Mentor(name=data['name'], email=data['email'], phone=data['phone'], linked_user=user)
        mentor.save()

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['name', 'email', 'phone', 'orgn', 'inn', 'kpp', 'bank', 'director', 'bik', 'city', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data, user):
        company = Company(name=data['name'], email=data['email'], phone=data['phone'], linked_user=user)
        company.save()

class UniversitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = University
        fields = ['name', 'email', 'phone', 'orgn', 'inn', 'kpp', 'bank', 'director', 'bik', 'city', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data, user):
        univer = University(name=data['name'], email=data['email'], phone=data['phone'], linked_user=user)
        univer.save()

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, to_custom_user, to_serializer):

        if to_custom_user['role'] == 'student':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'])
            user.set_password(to_custom_user['password'])
            user.save()
            StudentSerializer.create(StudentSerializer, to_serializer, user)
        elif to_custom_user['role'] == 'mentor':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'])
            user.set_password(to_custom_user['password'])
            user.save()
            MentorSerializer.create(MentorSerializer, to_serializer, user)
        elif to_custom_user['role'] == 'company':
            user = CustomUser(username=to_custom_user['inn'], email=to_custom_user['email'], inn=to_custom_user['inn'])
            user.set_password(to_custom_user['password'])
            user.save()
            CompanySerializer.create(CompanySerializer, to_serializer, user)
        elif to_custom_user['role'] == 'university':
            user = CustomUser(username=to_custom_user['inn'], email=to_custom_user['email'], inn=to_custom_user['inn'])
            user.set_password(to_custom_user['password'])
            user.save()
            UniversitySerializer.create(UniversitySerializer, to_serializer, user)

        return user

# class BonusTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BonusTransaction
#         fields = ['id', 'user', 'account_payment', 'value', 'note'] #'date_created', 'date_updated']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone']# 'date_created', 'date_updated']

# class BonusTransactionSerializer(serializers.ModelSerializer):
#     supplier_service = serializers.SerializerMethodField()
#     date_created = serializers.DateTimeField()

#     class Meta:
#         model = BonusTransaction
#         fields = ['id', 'user', 'value', 'note', 'date_created', 'supplier_service']

#     def get_supplier_service(self, obj):
#         result_dict = {}
#         try:
#             for item in AccountPaymentService.objects.filter(account_payment=obj.account_payment.id):
#                 result_dict[item.supplier_name] = item.service_name
#         except Exception: pass
#         if result_dict: return result_dict
#         else: return None
            