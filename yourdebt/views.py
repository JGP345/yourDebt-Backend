from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OpenDebtSerializer, CloseDebtSerializer, MortgageSerializer, UserSerializer, GroupSerializer
from .models import OpenDebt,CloseDebt,Mortgage
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt import authentication

# Create your views here.

class OpenDebtView(viewsets.ModelViewSet):
    serializer_class = OpenDebtSerializer
    queryset = OpenDebt.objects.all()
    permission_classes= [IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication)
class CloseDebtView(viewsets.ModelViewSet):
    serializer_class = CloseDebtSerializer
    queryset = CloseDebt.objects.all()
    permission_classes= [IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication)
class MortgageView(viewsets.ModelViewSet):
    serializer_class = MortgageSerializer
    queryset = Mortgage.objects.all()
    permission_classes= [IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication)
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = (authentication.JWTAuthentication)
# Create your views here.
