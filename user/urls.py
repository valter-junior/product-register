from django.conf.urls import url
from .views import UserLogin, UserRegistration

urlpatterns = [
    url('signup', UserRegistration.as_view()),
    url(r'^signin', UserLogin.as_view()),
    ]