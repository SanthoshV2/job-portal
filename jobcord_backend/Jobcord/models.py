from django.db import models

# Create your models here.
class JobApplication(models.Model):
    company_name=models.CharField(max_length=100) 
    job_title=models.CharField(max_length=100)
    status=models.CharField(max_length=50,
                            choices=[
                                ("applied","Applied"),
                                ("interview","Interview"),
                                ("offer","Offer"),
                                ("rejected","Rejected")
                            ])
    applied_date=models.DateField()
    notes=models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name}-{self.job_title}"


class Resume (models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.full_name

class PublicJobPost(models.Model):
    company_name=models.CharField(max_length=100) 
    job_title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    job_type=models.CharField(max_length=50,
                              choices=[('Full_time','Full_time'),
                                       ('Part_time', 'Part_time'),
                                       ('Internship', 'Internship')])
    description=models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


        
    
