from . import views
from django.urls import path

urlpatterns = [
    # /api-auth/login
    path('api/messages/<int:sender>/<int:receiver>', views.list_of_messages),
    path('api/messages/', views.list_of_messages),
    path('api/users/<int:id_primary_key>', views.list_of_users),
    path('api/users/', views.list_of_users)
]

