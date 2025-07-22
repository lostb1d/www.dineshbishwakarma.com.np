from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.HomePageView.as_view(), name='home'),

    # My Information
    path('myinformation/', views.MyInformationListView.as_view(), name='myinformation-list'),

    # Carousel (Photos)
    path('carousel/', views.CarouselPhotoListView.as_view(), name='carouselphoto-list'),

    # Work Information
    path('work/', views.WorkInformationListView.as_view(), name='workinformation-list'),

    # Experiences
    path('experience/', views.ExperienceListView.as_view(), name='experience-list'),

    # My Projects
    path('projects/', views.MyProjectListView.as_view(), name='myproject-list'),

    # Certifications
    path('certifications/', views.CertificationListView.as_view(), name='certification-list'),

    # Skills
    path('skills/', views.SkillListView.as_view(), name='skill-list'),

    # Blog - List and Detail
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),

    # Feedback / Contact (Create form for feedback)
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-list'),
]
