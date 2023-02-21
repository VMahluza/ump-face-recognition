from django.urls import path
from . import views

app_name = 'ump_biometrics'
urlpatterns = [
    path('student/<int:StudentNumber>', views.student, name='student'),
]