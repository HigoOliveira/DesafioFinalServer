from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny

from rest_framework import mixins
from rest_framework import generics

class UserVerify(mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'phone'

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

class Create(mixins.CreateModelMixin, generics.GenericAPIView):
  serializer_class = UserSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)