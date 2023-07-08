from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pictures, name='all-pictures'),
    path('members', views.members, name="members"),
    path('view/<pk>/', views.view, name="view"),
    path('details/<pk>/', views.details, name='details'),
    path('create', views.create, name='create'),
    path('update/<pk>/', views.update, name='update'),
    path('delete/<pk>/', views.delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)