from django.contrib import admin
# Register your models here.
from .models import JobApplication, PublicJobPost, Resume

@admin.register(JobApplication)    #register your model it appers in admin
class JobApplicationAdmin(admin.ModelAdmin):
    list_display=('company_name','job_title','status','applied_date')
    search_fields=('company_name','job_title')
    list_filter=('status','applied_date')


@admin.register(PublicJobPost) # Register PublicJobPost with a custom admin class
class PublicJobPostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'location', 'job_type', 'posted_at')
    search_fields = ('job_title', 'company_name', 'location')
    list_filter = ('job_type', 'posted_at')
    date_hierarchy = 'posted_at' # Adds a date navigation bar

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email', 'skills')