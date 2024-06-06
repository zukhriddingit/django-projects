from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Message, Group
from .serializers import MessageSerializer, GroupSerializer

# Create your views here.

# class IsGroupMember(permissions.BasePermission):
#     def has_permission(self, request, view):
#         group_id = view.kwargs.get('group_id')
#         group = Group.objects.get(pk = group_id)
#         return request.user in group.users.all()

class GroupMessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Message.objects.filter(group_id=group_id)
    
    def perform_create(self, serializer):
        group_id = self.kwargs['group_id']
        group = Group.objects.get(pk = group_id)
        serializer.save(author=self.request.user, group=group)
    
    permission_classes = [IsGroupMember]
    
# class to create new chat groups

class GroupCreateAPIView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication

    
class GroupMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsGroupMember]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({"error": "You can only delete your own messages"}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
