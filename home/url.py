from django.conf.urls import url
from .views import landing, auth, sign_out, apt_detail,\
                   ll_detail, create, apt_delete, ll_delete,\
                   create_apt, create_ll, edit, edit_ll,\
                   edit_apt, show_logs

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^logs', show_logs, name='logs'),
    url(r'^login', auth, name='login'),
    url(r'^sign_out$', sign_out, name='sign_out'),
    url(r'^create$', create, name='create'),
    url(r'^create_apt$', create_apt, name='create_apt'),
    url(r'^create_ll$', create_ll, name='create_ll'),
    url(r'^apt(?P<id>\d+)$', apt_detail, name='apt_detail'),
    url(r'^ll(?P<id>\d+)$', ll_detail, name='ll_detail'),
    url(r'^edit(?P<cat>\d+)id(?P<id>\d+)$', edit, name='edit'),
    url(r'^edit_apt(?P<id>\d+)$', edit_apt, name='edit_apt'),
    url(r'^edit_ll(?P<id>\d+)$', edit_ll, name='edit_ll'),
    url(r'^d_apt(?P<id>\d+)$', apt_delete, name='apt_delete'),
    url(r'^d_ll(?P<id>\d+)$', ll_delete, name='ll_delete'),
]
