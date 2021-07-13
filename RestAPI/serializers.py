from API.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    class Meta:
        model = Profile
        fields = ('name', 'email', 'phone','password','password2')
        extra_kwargs = {
            'password' : {'write_only' : True} 
        }
    def save(self):
        user = Profile(
            email = self.validated_data['email'],
            name = self.validated_data['name'],
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords do not match'})
        user.set_password(password)
        user.save()
        return user