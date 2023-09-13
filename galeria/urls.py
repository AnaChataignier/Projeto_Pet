from django.urls import path
from galeria.views import index, imagem, buscar, cadastro_pet, editar_pet, deletar_pet, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('cadastro_pet', cadastro_pet, name= 'cadastro_pet'),
    path('editar_pet/<int:foto_id>', editar_pet, name= 'editar_pet'),
    path('deletar_pet/<int:foto_id>', deletar_pet, name='deletar_pet' ),
    path('filtro/<str:categoria>', filtro, name='filtro' )
    
    
]