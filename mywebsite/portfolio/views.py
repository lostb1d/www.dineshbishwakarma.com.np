from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django import forms

from .models import (
    MyInformation, CarouselPhoto, WorkInformation, Experience,
    MyProject, Certification, Skill, Blog, Comment, Event, Feedback
)

# --- Forms ---

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

# --- Views ---

class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myinfo'] = MyInformation.objects.first()
        context['carousel_photos'] = CarouselPhoto.objects.all()[:6]
        context['workinfos'] = WorkInformation.objects.order_by('-start_date')[:3]
        context['experiences'] = Experience.objects.order_by('-start_date')[:3]
        context['projects'] = MyProject.objects.order_by('-start_date')[:3]
        context['skills'] = Skill.objects.all()[:8]
        context['certifications'] = Certification.objects.order_by('-date_issued')[:3]
        context['blogs'] = Blog.objects.order_by('-created_at')[:2]
        context['events'] = Event.objects.order_by('-start_datetime')[:2]
        return context

# Info & gallery
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
    context_object_name = 'projects'

class MyProjectDetailView(DetailView):
    model = MyProject
    template_name = "portfolio/myproject_detail.html"
    context_object_name = 'project'

class CertificationListView(ListView):
    model = Certification
    template_name = "portfolio/certification_list.html"
    context_object_name = 'certifications'

class SkillListView(ListView):
    model = Skill
    template_name = "portfolio/skill_list.html"

class EventListView(ListView):
    model = Event
    template_name = "portfolio/event_list.html"
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = "portfolio/event_detail.html"
    context_object_name = 'event'

# --- Blog & Comments ---

class BlogListView(ListView):
    model = Blog
    template_name = "portfolio/blog_list.html"
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = "portfolio/blog_detail.html"
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(approved=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = self.object
            comment.save()
            return redirect('portfolio:blog-detail', pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context['comment_form'] = comment_form
        return self.render_to_response(context)

# --- Feedback/Contact ---

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "portfolio/feedback_form.html"
    success_url = reverse_lazy('portfolio:home')
