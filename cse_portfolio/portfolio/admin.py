from django.contrib import admin

# Register your models here.
from .models import Project, Course, Certification


from .models import Project, Course, Certification

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed')
    search_fields = ('title',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'completion_date')
    search_fields = ('name', 'institution')

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issued_by', 'date_issued')
    search_fields = ('name', 'issued_by')
    
    
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Certification)