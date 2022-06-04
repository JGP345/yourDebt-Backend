from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OpenDebtSerializer, CloseDebtSerializer, MortgageSerializer
from .models import OpenDebt,CloseDebt,Mortgage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class OpenDebtView(viewsets.ModelViewSet):
    serializer_class = OpenDebtSerializer
    queryset = OpenDebt.objects.all()
class CloseDebtView(viewsets.ModelViewSet):
    serializer_class = CloseDebtSerializer
    queryset = CloseDebt.objects.all()
class MortgageView(viewsets.ModelViewSet):
    serializer_class = MortgageSerializer
    queryset = Mortgage.objects.all()
# Create your views here.
