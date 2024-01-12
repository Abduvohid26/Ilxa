from shared.views import generate_sms_code_api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView

from .models import User, SMSVerification
from .serializers import RegisterSerializer
from twilio.rest import Client

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate and send SMS code
        phone = request.data['phone']
        sms_verification, created = SMSVerification.objects.get_or_create(phone=phone)

        if not created:
            sms_verification.code = generate_sms_code_api()  # Implement your SMS code generation logic
        else:
            sms_verification.code = generate_sms_code_api()

        # Send SMS code
        try:
            self.send_sms(phone, sms_verification.code)
        except Exception as e:
            # Handle Twilio API exception
            return Response({'error': f'Error sending SMS: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        sms_verification.save()

        # Continue with user registration
        user = serializer.save()

        # You may want to generate JWT tokens and send them in the response for immediate login
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token, 'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    def send_sms(self, to, body):
        account_sid = 'AC757cbf920fb9ed6abf1319d759acca27'
        auth_token = '5f1fd7303d144fb6a28ee73fece9d9f0'
        twilio_phone_number = '+12059318108'

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to
        )

        print(f"SMS sent to {to}: {message.sid}")

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=204)

