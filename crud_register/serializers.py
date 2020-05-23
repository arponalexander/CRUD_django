from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company_B00, Insurance_B00, Insurance_B01


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company_B00
        fields = '__all__'


class InsuranceB00Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance_B00
        fields = '__all__'


class InsuranceB01Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance_B01
        fields = '__all__'
