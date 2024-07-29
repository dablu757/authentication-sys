from rest_framework import serializers
from account.models import User

#registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2','tc']
        extra_kwargs={
            'password' : {'write_only' : True}
        }


    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("password and conform password does't matches")
        return attrs
    

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    

#login serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email', 'password']