from django.shortcuts import render
from rest_framework import viewsets
from .models import Company_B00, Insurance_B00, Insurance_B01
from .serializers import CompanySerializer, InsuranceB00Serializer, InsuranceB01Serializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company_B00.objects.all()
    serializer_class = CompanySerializer


class InsuranceB00View(viewsets.ModelViewSet):
    queryset = Insurance_B00.objects.all()
    serializer_class = InsuranceB00Serializer


class InsuranceB01View(viewsets.ModelViewSet):
    queryset = Insurance_B01.objects.all()
    serializer_class = InsuranceB01Serializer
