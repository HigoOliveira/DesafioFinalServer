from rest_framework.views import APIView
from .models import User, Event
from .serializer import UserSerializer, EventSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework import status, mixins, generics
from rest_framework.response import Response

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
    data = request.data.copy()
    data['user'] = self.request.user.id
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ListEvent(mixins.ListModelMixin, generics.GenericAPIView):
  permissioon_classes = (IsAuthenticated,)
  queryset = Event.objects.all()
  serializer_class = EventSerializer

  def get_queryset(self):
    queryset = super(ListEvent, self).get_queryset()
    return queryset.filter(user=self.request.user)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

class DeleteEvent(mixins.DestroyModelMixin, generics.GenericAPIView):
  serializer_class = EventSerializer
  permissioon_classes = (IsAuthenticated,)
  queryset = Event.objects.all()

  def post(self, request, *args, **kwargs):
    print(request.POST)
    return self.destroy(request, *args, **kwargs)