"""employeeCRUD_using_APIViews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', views.EmployeeAPIView.as_view()),
    path('api/', views.EmployeeListAPIView.as_view()),
    path('api_create/', views.EmployeeCreateAPIView.as_view()),
    path('api_retrieve/<int:pk>/', views.EmployeeRetrieveAPIView.as_view()),
    path('api_update/<int:pk>/', views.EmployeeUpdateAPIView.as_view()),
    path('api_destroy/<int:pk>/', views.EmployeeDestroyAPIView.as_view()),
    path('api_list_create/', views.EmployeeListCreateAPIView.as_view()),
    path('api_retrieve_update/<int:pk>/', views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('api_retrieve_destroy/<int:pk>/', views.EmployeeDestroyAPIView.as_view()),
    path('api_retrieve_update_destroy/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('api_list_mixin/', views.EmployeeListModelMixin.as_view()),
    path('api_retrieve_update_destroy_mixin/<int:pk>', views.EmployeeRetrieveUpdateDestroyMixin.as_view()),

]
