from django.urls import path
from Tutor.views import cadastro_tutor


urlpatterns = [
   path('cadastro_tutor', cadastro_tutor, name='cadastro_tutor'),
]