from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.blogpost,name="new"),
    path('<int:blog_id>/edit/', views.edit, name="edit"),
    path('<int:blog_id>/delete/', views.delete, name="delete")
]