from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile, Portfolio, Skill, Testimonial, PortfolioSkill, Contact
from .forms import ContactForm
from django.core.mail import send_mail

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
    profile = Profile.objects.get(id=1)
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['helloworld@gmail.com'],
            )
            form.save()
            submitted=True
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'port/contact.html', {'form': form, 'submitted': submitted, 'profile': profile})

def term(request):
    return render(request, 'port/term.html')

def privacy(request):
    return render(request, 'port/privacy.html')

def cookies(request):
    return render(request, 'port/cookies.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        portfolio_lists = Portfolio.objects.filter(is_published=True)
        results = portfolio_lists.filter(name__icontains=searched)
        return render(request, 'port/search.html', {'searched': searched, 'results': results})
    return render(request, 'port/search.html')

def download_resume(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='resume')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
