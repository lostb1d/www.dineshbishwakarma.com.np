from django.contrib import admin
from .models import (
    MyInformation,
    CarouselPhoto,
    WorkInformation,
    Experience,
    MyProject,
    Certification,
    Skill,
    Blog,
    Comment,
    Event,
    Feedback,
)

@admin.register(MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_email', 'contact_phone')
    search_fields = ('full_name', 'contact_email')

@admin.register(CarouselPhoto)
class CarouselPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)

@admin.register(WorkInformation)
class WorkInformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'office', 'start_date', 'end_date')
    search_fields = ('title', 'department', 'office')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'organization', 'start_date', 'end_date', 'location')
    search_fields = ('position', 'organization', 'location')

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'start_date', 'end_date')
    search_fields = ('title', 'role', 'technologies')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_issued', 'credential_id')
    search_fields = ('name', 'issuer', 'credential_id')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name', 'proficiency')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'email', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_datetime', 'end_datetime', 'organizer')
    search_fields = ('title', 'location', 'organizer')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    readonly_fields = ('submitted_at',)
