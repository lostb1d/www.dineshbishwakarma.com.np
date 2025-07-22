from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import (
    MyInformation,
    CarouselPhoto,
    WorkInformation,
    Experience,
    MyProject,
    Certification,
    Skill,
    Blog,
    Feedback
)

# Homepage view: aggregates data for summary overview
class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myinfo'] = MyInformation.objects.first()
        context['carousel_photos'] = CarouselPhoto.objects.all()[:6]
        context['workinfo'] = WorkInformation.objects.order_by('-start_date').first()
        context['experiences'] = Experience.objects.order_by('-start_date')[:2]
        context['projects'] = MyProject.objects.order_by('-start_date')[:2]
        context['skills'] = Skill.objects.all()[:8]
        context['certifications'] = Certification.objects.order_by('-date_issued')[:3]
        context['blogs'] = Blog.objects.order_by('-created_at')[:2]
        return context


# List Views for each section
class MyInformationListView(ListView):
    model = MyInformation
    template_name = "portfolio/myinformation_list.html"

class CarouselPhotoListView(ListView):
    model = CarouselPhoto
    template_name = "portfolio/carouselphoto_list.html"

class WorkInformationListView(ListView):
    model = WorkInformation
    template_name = "portfolio/workinformation_list.html"

class ExperienceListView(ListView):
    model = Experience
    template_name = "portfolio/experience_list.html"

class MyProjectListView(ListView):
    model = MyProject
    template_name = "portfolio/myproject_list.html"

class CertificationListView(ListView):
    model = Certification
    template_name = "portfolio/certification_list.html"

class SkillListView(ListView):
    model = Skill
    template_name = "portfolio/skill_list.html"

class BlogListView(ListView):
    model = Blog
    template_name = "portfolio/blog_list.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "portfolio/blog_detail.html"

# class BlogCreateView(CreateView):
#     model = Blog
#     fields = ['title', 'content', 'thumbnail']
#     template_name = "portfolio/blog_form.html"
    success_url = reverse_lazy('blog-list')

# class BlogUpdateView(UpdateView):
#     model = Blog
#     fields = ['title', 'content', 'thumbnail']
#     template_name = "portfolio/blog_form.html"
#     success_url = reverse_lazy('blog-list')

# Feedback Create View (Contact form)
class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'email', 'message']
    template_name = "portfolio/feedback_list.html"
    success_url = reverse_lazy('feedback-list')
