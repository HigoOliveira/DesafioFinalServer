from rest_framework import serializers

from .models import User, Event

class UserSerializer(serializers.ModelSerializer):
  name = serializers.CharField(required=False, allow_blank=True, default='')
  password = serializers.CharField(write_only=True, required=False, allow_blank=True, default='')
  password_confirm = serializers.CharField(write_only=True, required=False, allow_blank=True, default='')

  def validate(self, data):
    if not self.instance:
      return data
    if not data.get('password') and data.get('password') != data.get('password_confirm'):
      raise serializers.ValidationError("Those passwords don't match.")
    return data

  def update(self, instance, validated_data):
    if validated_data['password'] != '':
      instance.set_password(validated_data['password'])
    if validated_data['name'] != '':
      instance.name = validated_data['name']
    instance.save()
    return instance

  def create(self, validated_data):
    password = validated_data['password']
    del validated_data['password']
    del validated_data['password_confirm']
    user = super(UserSerializer, self).create(validated_data)
    user.set_password(password)
    user.save()

    return user
  class Meta:
    model = User
    fields = ('phone', 'name', 'password', 'password_confirm')
    
class EventSerializer(serializers.ModelSerializer):

  # def create(self, validated_data):
  #   event = super(EventSerializer, self).create(validated_data)
  #   event.user = 
  #   event.save()

  #   return event
  class Meta:
    model = Event
    fields = '__all__'