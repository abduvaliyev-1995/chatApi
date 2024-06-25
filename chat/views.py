from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MsgListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MsgDestroyAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MsgRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SecureView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'This is a secure message'})
