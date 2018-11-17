
# Create your views here.


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.response import Response

from . import  models
from . import  serializers

from  django.contrib.auth.models import User
from rest_framework.authtoken.models import Token





class Index(TemplateView):

     def get(self, request, *args, **kwargs):
         return HttpResponse('Empty Page')

class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        token = Token.objects.create(user=user)

        return Response({'details': 'User has been Created with Token  '+token.key} )





class ChangePassword(generics.CreateAPIView) :
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
         user = get_object_or_404(User, username=request.user)
         user.set_password(request.POST.get('new_password'))
         user.save()

         return Response({'details': 'Password Has been save.'})










class Transaksi(generics.ListCreateAPIView):
    queryset = models.Transksi.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TransaksiSerializer


    def perform_create(self, serializer):
        serializer.save(prmilik=self.request.user)



class TransaksiModifikasi(generics.RetrieveUpdateDestroyAPIView ):
    queryset = models.Transksi.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TransaksiSerializer


    def get_queryset(self):
        return models.Transksi.objects.filter(prmilik=self.request.user)


    def get_object(self):
        return get_object_or_404(models.Transksi, pk=self.kwargs['transaksi_id'])