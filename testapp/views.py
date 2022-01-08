from typing import Generic
from django.db.models.query import QuerySet
from django.shortcuts import render
from testapp.models import Employee
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from testapp.serializers import EmployeeSerializers
from rest_framework.response import Response 
# Create your views here.
#mixins
class EmployeeListModelMixin(CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeRetrieveUpdateDestroyMixin(UpdateModelMixin,DestroyModelMixin,RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 

'''
class EmployeeAPIView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeSerializers(qs,many=True) #job of serializers convert complex data instance to python ddict datatype
        return Response(serializer.data)   #serializer.data this is python dict, Response is convert python to json 
'''
#generics classess
class EmployeeListAPIView(ListAPIView):
    # queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains='raj')    #only displayed details who's name is raj
        return qs

class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
