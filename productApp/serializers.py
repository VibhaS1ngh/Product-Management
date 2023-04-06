from rest_framework import serializers
from productApp.models import User, Product


class UserRegistrationSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['name', 'email', 'mobile', 'password', 'confirm_password']
    extra_kwargs={
      'password':{'write_only':True}
    }

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('confirm_password')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    validate_data['username'] = validate_data['email'].split("@")[0]
    data = {k: v for k, v in validate_data.items() if k in ['name', 'username', 'email', 'mobile', 'password']}
    return User.objects.create_user(**data)


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"