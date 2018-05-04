from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    # url(r'^account/login/$', views.user_login),

    # create account
    url(r'^registration/$', views.register,  name='register'),
    # login and logout
    url(r'^login/$', 'django.contrib.auth.views.login',  name='login'),
    # edit user data and profile
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'registration/log_out.html'}, name='logout'),

    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout-then-login'),

    # password change
    url(r'^account/password-change/$',
        'django.contrib.auth.views.password_change',
        {'template_name': 'registration/password_change.html'},
        name='change_password'),

    url(r'^account/password-change/done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'registration/change_done.html'},
        name='password_change_done'),

    # password reset
    url(r'^password-rest/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'registration/password-rest-form.html',
         }, name='password_rest'),

    url(r'^password-rest/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'registration/password-rest-done.html'}, name='password_reset_done'),

    url(r'^password-rest/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'registration/password-rest-confirm.html'}, name='password_reset_confirm'),

    url(r'^password-rest/complete/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'registration/password-rest-complete.html'}, name='password_reset_complete'),

]
