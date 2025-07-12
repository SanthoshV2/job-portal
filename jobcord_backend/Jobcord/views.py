from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, generics
from .models import JobApplication, Resume, PublicJobPost
from .serializers import JobApplicationSerializer, ResumeSerializer, PublicJobPostSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):  #Automatically creates CRUD APIs
    queryset=JobApplication.objects.all()           #Fetches all job application from database
    serializer_class=JobApplicationSerializer    #Tells Django how to converts model to JSON


class ResumeCreateView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class PublicJobPostListAPIView(generics.ListAPIView):
    queryset = PublicJobPost.objects.all().order_by('-posted_at')
    serializer_class = PublicJobPostSerializer