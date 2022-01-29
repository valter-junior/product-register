from django.conf.urls import url
from .views import UserLogin, UserRegistration

urlpatterns = [
    url(r'^signup', UserRegistration.as_view()),
    url(r'^signin', UserLogin.as_view()),
    ]