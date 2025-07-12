from rest_framework import serializers
from .models import JobApplication, Resume, PublicJobPost

class JobApplicationSerializer(serializers.ModelSerializer): #shortcut to convert model into JSON automatically
    class Meta:
        model = JobApplication
        fields = '__all__'   # Use all field in the model(Company_name,status etc)


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields= '__all__'


class PublicJobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicJobPost
        fields = '__all__'
        