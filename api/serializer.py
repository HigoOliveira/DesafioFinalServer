from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
  name = serializers.CharField(required=False, allow_blank=True, default='')
  password = serializers.CharField(write_only=True, required=False, allow_blank=True, default='')
  password_confirm = serializers.CharField(write_only=True, required=False, allow_blank=True, default='')

  def validate(self, data):
    if not data.get('password') or not data.get('password_confirm'):
      raise serializers.ValidationError("Please enter a passwrod and confirm it.")
    
    if data.get('password') != data.get('password_confirm'):
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
    user = super(UserSerializer, self).create(validated_data)
    user.set_password(validated_data['password'])
    user.save()

    return user
  class Meta:
    model = User
    fields = ('phone', 'name', 'password', 'password_confirm')
    
    