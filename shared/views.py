
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import SMSVerification
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def generate_sms_code_api(request):
#     user = request.user
#     sms_verification, created = SMSVerification.objects.get_or_create(user=user)
#
#     if not created:
#         sms_verification.code = get_random_string(length=4, allowed_chars='0123456789')
#         sms_verification.is_verified = False
#         print(sms_verification)
#         sms_verification.save()
#
#         # Implement SMS sending logic here
#
#         return Response({'detail': 'SMS code has been sent to your phone.'}, status=status.HTTP_200_OK)
#     else:
#         # Implement SMS sending logic here
#
#         return Response({'detail': 'SMS code has been sent to your phone.'}, status=status.HTTP_200_OK)
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def verify_sms_code_api(request):
#     user = request.user
#     sms_code = request.data.get('sms_code')
#     sms_verification = SMSVerification.objects.get(user=user)
#
#     if sms_verification.code == sms_code:
#         sms_verification.is_verified = True
#         print(sms_code)
#         sms_verification.save()
#         return Response({'detail': 'SMS code has been verified successfully.'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'detail': 'Invalid SMS code. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_sms_code_api(request):
    user = request.user
    sms_verification, created = SMSVerification.objects.get_or_create(user=user)

    if not created:
        sms_verification.code = get_random_string(length=4, allowed_chars='0123456789')
        sms_verification.is_verified = False
        sms_verification.save()

        # SMS yuborish logikasini shu joyda amalga oshiring
        print(f"SMS code: {sms_verification.code} has been sent to {user}'s phone.")

        return Response({'detail': 'SMS code has been sent to your phone.'}, status=status.HTTP_200_OK)
    else:
        # SMS yuborish logikasini shu joyda amalga oshiring
        print(f"SMS code: {sms_verification.code} has been sent to {user}'s phone.")

        return Response({'detail': 'SMS code has been sent to your phone.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_sms_code_api(request):
    user = request.user
    sms_code = request.data.get('sms_code')
    sms_verification = SMSVerification.objects.get(user=user)

    if sms_verification.code == sms_code:
        sms_verification.is_verified = True
        sms_verification.save()
        print(f"SMS code: {sms_verification.code} has been verified successfully for {user}.")
        return Response({'detail': 'SMS code has been verified successfully.'}, status=status.HTTP_200_OK)
    else:
        print(f"Invalid SMS code entered for {user}.")
        return Response({'detail': 'Invalid SMS code. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)
