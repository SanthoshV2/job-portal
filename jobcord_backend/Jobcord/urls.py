from django.urls import path, include
from rest_framework import routers
from .views import JobApplicationViewSet, ResumeCreateView, PublicJobPostListAPIView


router=routers.DefaultRouter()   #Automatically maps routes to the viewset
router.register(r'application',JobApplicationViewSet)  #Adds API route

urlpatterns=[
    path('',include(router.urls)),  #connects the router to URL system

    path('resume/',
         ResumeCreateView.as_view(),
         name='resume-create'),
                    
                    
    path('jobs/',PublicJobPostListAPIView.as_view(),
         name='public-job-list'),
]

