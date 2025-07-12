from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    user_type = models.CharField(max_length=20, 
                                 choices=[('job_seeker', 'Job Seeker'), 
                                          ('employer', 'Employer')],
                                            default='job_seeker')
    
    def __str__(self):
        return self.username


