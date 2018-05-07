from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer, EventSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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

class Update(mixins.UpdateModelMixin, generics.GenericAPIView):
  permissioon_classes = (IsAuthenticated,)
  serializer_class = UserSerializer
  queryset = User.objects.all()

  def get_object(self):
    return self.request.user
    
  def post(self, request, *args, **kwargs):
    return self.partial_update(request, *args, **kwargs)

class CreateEvent(mixins.CreateModelMixin, generics.GenericAPIView):
  permissioon_classes = (IsAuthenticated,)
  serializer_class = EventSerializer
  def post(self, request, *args, **kwargs):
    print(request)
    return self.create(request, *args, **kwargs)