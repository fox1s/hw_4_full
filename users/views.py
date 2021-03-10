from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import UserModel
from users.serializers import UserSerializer


class ListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = UserModel.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        return qs


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
