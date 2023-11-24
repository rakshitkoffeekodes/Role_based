from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import *
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.

@api_view(['POST'])
def auth_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({'msg': 'Success', 'refresh': str(refresh), 'access': str(refresh.access_token)})
    else:
        return JsonResponse({'status': 'User Not exist'})



@api_view(['POST'])
def add_role(request):
    ur_role = request.data.get('ur_role')
    UserRole.objects.create(
        ur_role=ur_role,
        created_at=datetime.now()
    )
    return JsonResponse({'status': 'Add Role'})


@api_view(['GET'])
def all_role(request):
    All = UserRole.objects.all()
    serial = UserRoleSerializer(All, many=True)
    return JsonResponse(serial.data)


@api_view(['DELETE'])
def delete_role(request, pk):
    dlt = UserRole.objects.get(id=pk)
    dlt.delete()
    serial = UserRoleSerializer(dlt)
    return JsonResponse(serial.data)


@api_view(['PUT'])
def update_role(request, pk):
    up = UserRole.objects.get(id=pk)
    ur_role = request.data.get('ur_role')
    if up:
        up.ur_role = ur_role
        up.save()
        return JsonResponse({'status': 'Update success'})

    else:
        return JsonResponse({'status': 'ID not exist'})


@api_view(['POST'])
def auth_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    User.objects.create(
        username=username,
        password=password
    )
    return JsonResponse({'status': 'Success'})


@api_view(['POST'])
def register(request):
    ur_id = request.data.get('ur_id')
    user_name = request.data.get('user_name')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    mobile_no = request.data.get('mobile_no')
    email = request.data.get('email')
    dob = request.data.get('dob')
    password = request.data.get('password')

    if len(mobile_no) == 10:
        try:
            role = UserRole.objects.get(ur_id=ur_id)
            UserDetails.objects.create(
                ur_id=role,
                user_name=user_name,
                first_name=first_name,
                last_name=last_name,
                mobile_no=mobile_no,
                email=email,
                dob=dob,
                password=password,
                created_at=datetime.now()
            )
            return JsonResponse({'status': 'registration success'})
        except Exception as e:
            return JsonResponse({'msg': str(e)})
    else:
        return JsonResponse({'status': 'Mobile number must be 10 digits'})


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = UserDetails.objects.get(email=email)
        if user.password == password:
            request.session['email'] = email
            return JsonResponse({'status': 'login'})
        else:
            return JsonResponse({'status': 'Password does not match'})
    except Exception as e:
        return JsonResponse({'status': e.__str__()})
