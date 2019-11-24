from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.contrib.auth import models, authenticate, login, logout
import json
from django.core import serializers
from django.db.models import Avg, Count, Sum, FloatField
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.parsers import JSONParser
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def log_in(request):
    return render(request, 'uber/mycustomlogin.html')

def authenticate(request):
    # request.user.is_authenticated = True
    print(request.user)
    return HttpResponse()