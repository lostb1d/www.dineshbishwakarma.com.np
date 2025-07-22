from django.contrib import admin
from .models import (
    MyInformation, CarouselPhoto, WorkInformation, Experience, MyProject,
    Certification, Skill, Blog, Feedback
)

admin.site.register(MyInformation)
admin.site.register(CarouselPhoto)
admin.site.register(WorkInformation)
admin.site.register(Experience)
admin.site.register(MyProject)
admin.site.register(Certification)
admin.site.register(Skill)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'thumbnail']
    
admin.site.register(Feedback)
