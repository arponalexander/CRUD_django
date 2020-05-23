from django.urls import path,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Company_B00', views.CompanyView)
routers.register('Insurance_B00', views.InsuranceB00View)
routers.register('Insurance_B01', views.InsuranceB01View)

urlpatterns = [
    path('', include(routers.urls))
]
