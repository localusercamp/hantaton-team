from rest_framework import serializers
from .models import *



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data, user):
        student = Student(name=data['name'], email=data['email'], phone=data['phone'], linked_user=user)
        user.save()

class MentorSerializer(serializers.ModelSerializer):
    pass

class CompanySerializer(serializers.ModelSerializer):
    pass

class UniversitySerializer(serializers.ModelSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, to_custom_user, to_serializer):
        user = ""

        if to_custom_user['role'] == 'student':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'])
            StudentSerializer.create(StudentSerializer, to_serializer, user)
        elif to_custom_user['role'] == 'mentor':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'])
            MentorSerializer.create(MentorSerializer, to_serializer, user)
        elif to_custom_user['role'] == 'company':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'], inn=to_custom_user['inn'])
            CompanySerializer.create(CompanySerializer, to_serializer, user)
        elif to_custom_user['role'] == 'university':
            user = CustomUser(username=to_custom_user['username'], email=to_custom_user['email'], inn=to_custom_user['inn'])
            UniversitySerializer.create(UniversitySerializer, to_serializer, user)

        user.set_password(to_custom_user['password'])
        user.save()
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
            