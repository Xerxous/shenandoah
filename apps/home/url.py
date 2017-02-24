from django.conf.urls import url
from .views import landing, auth

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^login/', auth, name='login'),
]
