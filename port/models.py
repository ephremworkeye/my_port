from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    age = models.PositiveIntegerField(blank=True)
    country = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=250, blank=True)
    zipcode = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='portfolio/%Y/%m/%d',blank=True)
    website = models.URLField(max_length=250, blank=True)
    github = models.URLField(max_length=250, null=True, blank=True)
    resume = models.FileField(upload_to='resume', null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    

class Portfolio(models.Model):
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, null=True)
    description = models.TextField(blank=True)
    website_link = models.URLField(max_length=250, blank=True)
    github_link = models.URLField(max_length=350, blank=True)
    skill = models.ManyToManyField('Skill', through='PortfolioSkill', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField(max_length=120)
    rate = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PortfolioSkill(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE,)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.portfolio }, { self.skill }'

class Testimonial(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    body = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=250, blank=True)
    message = models.TextField(blank=True)