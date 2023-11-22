from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from datetime import datetime


# Create your views here.

@api_view(['POST'])
def add_role(request):
    ur_role = request.data.get('ur_role')
    UserRole.objects.create(
        ur_role=ur_role,
        created_at=datetime.now()
    )
    content = {'status': 'Add Role'}
    return Response(content)


@api_view(['GET'])
def all_role(request):
    All = UserRole.objects.all()
    serial = UserRoleserializer(All, many=True)
    return Response(serial.data)


@api_view(['DELETE'])
def delete_role(request, pk):
    dlt = UserRole.objects.get(id=pk)
    dlt.delete()
    serial = UserRoleserializer(dlt)
    return Response(serial.data)


@api_view(['PUT'])
def update_role(request, pk):
    up = UserRole.objects.get(id=pk)
    ur_id = request.data.get('ur_id')
    ur_role = request.data.get('ur_role')
    if up:
        up.ur_id = ur_id
        up.ur_role = ur_role
        up.save()
        content = {'status': 'Update success'}
        return Response(content)

    else:
        content = {'status': 'invalid id'}
        return Response(content)


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
    role = UserRole.objects.get(ur_id=ur_id)
    if len(str(mobile_no)) == 10:
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
        content = {'status': 'registration success'}
        return Response(content)
    else:
        content = {'status': 'enter valid mobile number'}
        return Response(content)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            log = UserDetails.objects.get(email=email)
            if log.password == password:
                request.session['email'] = email
                content = {'status': 'login'}
                return Response(content)
            else:
                content = {'status': 'Password Not match'}
                return Response(content)
        except:
            content = {'status': 'Email not match'}
            return Response(content)
    else:
        content = {'status': 'login again'}
        return Response(content)
