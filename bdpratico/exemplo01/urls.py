from django.contrib import admin
from django.urls import path
from . import views

##Adicionando rotas das  paginas 6, 7, 8,9 10
urlpatterns = [
    path('', views.index, name = 'index_alias'),
    path('pagina0', views.pagina0, name = 'pagina0_alias'),
    path('pagina1', views.pagina1, name = 'pagina1_alias'),
    path('pagina2', views.pagina2, name = 'pagina2_alias'),
    path('pagina3', views.pagina3, name = 'pagina3_alias'),
    path('pagina4', views.pagina4, name = 'pagina4_alias'),
    path('pagina5', views.pagina5, name = 'pagina5_alias'),
    path('pagina6', views.pagina6, name = 'pagina6_alias'),
    path('pagina7', views.pagina7, name = 'pagina7_alias'),
    path('pagina8', views.pagina8, name = 'pagina8_alias'),
    path('pagina9', views.pagina9, name = 'pagina9_alias'),
    path('pagina10', views.pagina10, name = 'pagina10_alias'),
    path('pessoa_menu', views.pessoa_menu.as_view(), name = 'pessoa_menu_alias'),
    path("pessoa_list/", views.pessoa_list.as_view(), name = 'pessoa_list_alias'),
    path("pessoa_create/", views.pessoa_create.as_view(), name = 'pessoa_create_alias'),
    path("pessoa_update/<int:pk>/", views.pessoa_update.as_view(), name = 'pessoa_update_alias'),
    path('pessoa_delete/<int:pk>/', views.pessoa_delete.as_view(), name = 'pessoa_delete_alias'),
]
