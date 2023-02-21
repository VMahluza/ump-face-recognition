from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'ump_biometrics'
urlpatterns = [
    path('student/<int:StudentNumber>', views.student, name='student'),
    
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
