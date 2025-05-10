from django.urls import path
from .views import EmployeeListCreateView

urlpatterns = [
    path('create/', EmployeeListCreateView.as_view(), name='home'),

]
