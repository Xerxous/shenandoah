from django.conf.urls import url
from .views import landing, auth, sign_out, apt_detail, ll_detail

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^login', auth, name='login'),
    url(r'^sign_out$', sign_out, name='sign_out'),
    url(r'^apt(?P<id>\d+)$', apt_detail, name='apt_detail'),
    url(r'^ll(?P<id>\d+)$', ll_detail, name='ll_detail')
]
