from django.db import models

class MyInformation(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.full_name

class CarouselPhoto(models.Model):
    image = models.ImageField(upload_to='carousel/')
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.caption or f"Photo {self.pk}"

class WorkInformation(models.Model):
    title = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='workinformation/', null=True, blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='workinfo_blogs')

    def __str__(self):
        return self.title

class Experience(models.Model):
    position = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='experiences/', null=True, blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='experience_blogs')

    def __str__(self):
        return f"{self.position} at {self.organization}"

class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='myprojects/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    role = models.CharField(max_length=100, blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='project_blogs')

    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150)
    image = models.ImageField(upload_to='certifications/', null=True, blank=True)
    date_issued = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    certificate_url = models.URLField(blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='certification_blogs')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skill_icons/', null=True, blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='skill_blogs')

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    organizer = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    related_blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL, related_name='event_blogs')

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
