from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('myinformation/', views.MyInformationListView.as_view(), name='myinformation-list'),
    path('carousel/', views.CarouselPhotoListView.as_view(), name='carouselphoto-list'),
    path('work/', views.WorkInformationListView.as_view(), name='workinformation-list'),
    path('experience/', views.ExperienceListView.as_view(), name='experience-list'),
    path('projects/', views.MyProjectListView.as_view(), name='myproject-list'),
    path('projects/<int:pk>/', views.MyProjectDetailView.as_view(), name='myproject-detail'),
    path('certifications/', views.CertificationListView.as_view(), name='certification-list'),
    path('skills/', views.SkillListView.as_view(), name='skill-list'),
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-list'),
]
