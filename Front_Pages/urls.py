
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home,name="home"),
    path('resume/', resumes,name="resume"),
    path('contact/', contact,name="contact"),
    path('api/', api, name="api"),
]
