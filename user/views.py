from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from user.throttle import MyThrottling


# class UserAPIView(APIView):
#     throttle_classes = [MyThrottling]
#     def get(self,request,*args,**kwargs):
#         return Response("ok")
#
#     def post(self,request,*args,**kwargs):
#         return Response("post")

class UserAPIView(APIView):
    throttle_classes = [MyThrottling]

    def get(self, request, *args, **kwargs):
        return Response("OK")

    def post(self, request):
        return Response("写操作")

from rest_framework.filters import SearchFilter, OrderingFilter

class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer


    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "price"]

    ordering = ["price"]





