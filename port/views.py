from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile, Portfolio, Skill, Testimonial, PortfolioSkill, Contact
from .forms import ContactForm

# Create your views here.
def home(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    testimonial1 = Testimonial.objects.get(id=1)
    testimonial2 = Testimonial.objects.get(id=2)
    skills = Skill.objects.all()
    profile = Profile.objects.get(id=1)
    form = ContactForm()
        
    return render(request, 'port/home.html', {
        'portfolios':portfolios,
        'testimonial1':testimonial1,
        'testimonial2':testimonial2,
        'skills': skills,
        'profile': profile,
        'form': form,
    })

def detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    skills = portfolio.skill.all()
    return render(request, 'port/detail.html', {'portfolio': portfolio, 'skills': skills})

def about(request):
    profile = Profile.objects.get(id=1)
    skills = Skill.objects.all()
    return render(request, 'port/about.html', {'profile': profile, 'skills': skills})

def work(request):
    portfolios = Portfolio.objects.filter(is_published=True)

    return render(request, 'port/work.html', {'portfolios' :portfolios})

def contact(request):
    form = ContactForm()
    return render(request, 'port/contact.html', {'form':form})

def term(request):
    return render(request, 'port/term.html')

def privacy(request):
    return render(request, 'port/privacy.html')

def cookies(request):
    return render(request, 'port/cookies.html')

