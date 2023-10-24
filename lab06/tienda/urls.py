from django.urls import path

from . import views
from . import views as api_views

app_name = 'tienda'
urlpatterns = [
    path('', views.index, name="index"),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),

    path('api/categorias/', views.CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('api/categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('api/productos/', views.ProductoListCreateView.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
]


