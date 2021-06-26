from django.urls import path
from . import views

app_name = 'port'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/<slug:slug>/', views.detail, name='detail'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact'),
    path('term', views.term, name='term'),
    path('privacy', views.privacy, name='privacy'),
    path('cookies', views.cookies, name='cookies'),
    path('search', views.search, name='search'),
    path('download', views.download_resume, 'download'),

]
