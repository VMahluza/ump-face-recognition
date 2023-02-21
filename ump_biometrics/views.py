from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer

from ump_biometrics.models import Student

# Create your views here.

@api_view(['GET'])
def student(request, StudentNumber):
    if request.method == 'GET':

        try:

            if StudentNumber:

                student = Student.objects.get(StudentNumber=StudentNumber)
                serialized = StudentSerializer(student)
                return JsonResponse(serialized.data)

            else:
                return HttpResponse(status=404)
        except:
            return HttpResponse(status=401)

