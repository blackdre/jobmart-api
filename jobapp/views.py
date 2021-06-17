from rest_framework import generics
from .models import Jobs
from .serializers import JobSerializer


class JobList(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
