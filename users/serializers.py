from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import User, SMSVerification

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, required=True)
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    code = serializers.CharField(style={'input_type': 'code'}, required=False, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'phone', 'password', 'password_confirmation', 'code']

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match.')

        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')

        # Remove 'code' key from data before creating the User instance
        sms_code = data.pop('code', None)

        # Check if the user already exists
        user = User(**data)
        try:
            sms_verification = SMSVerification.objects.get(user=user)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('SMS verification not found for the user.')

        # Check if the provided SMS code matches
        if sms_verification.code != sms_code:
            raise serializers.ValidationError('Invalid SMS code. Please try again.')

        return data

    def create(self, validated_data):
        # Create the user using create_user to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            phone=validated_data['phone'],
            password=validated_data['password'],
        )

        # Set SMS verification as verified
        sms_verification = SMSVerification.objects.get(user=user)
        sms_verification.is_verified = True
        sms_verification.save()

        return user
