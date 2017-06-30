from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'myapp/index.html')


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes((IsAuthenticated,))
def home(request):
    return HttpResponse('Hi!')

