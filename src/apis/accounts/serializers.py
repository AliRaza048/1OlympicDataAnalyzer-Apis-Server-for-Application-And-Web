from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="This email is already in use.")]
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        code = user.verification_code

        return user




class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=4)

    def validate(self, data):
        email = data.get('email')
        code = data.get('verification_code')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email address")

        if user.verification_code != code:
            raise serializers.ValidationError("Invalid verification code")

        return data

    def save(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_verified = True
        user.verification_code = ''
        user.save()
        return user







