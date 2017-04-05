from django.conf.urls import url
from .views import landing, auth, sign_out

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^login/', auth, name='login'),
    url(r'^sign_out$', sign_out, name='sign_out')
]
