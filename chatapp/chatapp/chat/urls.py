from django.contrib import admin
from django.urls import path, include
from .views import GroupMessageDetail, GroupMessageListCreate
from rest_framework.authtoken import views as rest_views



urlpatterns = [
    path('groups/<int:group_id>/messages/', GroupMessageListCreate.as_view(), name='messages_list'),
    path('groups/<int:group_id>/messages/<int:pk>', GroupMessageDetail.as_view(), name='messages_detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', rest_views.obtain_auth_token, name='api-token-auth'),
]
