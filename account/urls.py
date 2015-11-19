from django.conf.urls import patterns, url

urlpatterns = patterns(
    'account.views',
    url(r'^(?P<user_id>\d+)/info/$',
        'user_info', name='user_info'),
    url(r'^reg/$', 'reg', name='reg'),
    url(r'^super/$', 'super_login', name='super_login'),
    url(r'^signin/$', 'user_login', name='signin'),
    url(r'^setting/$', 'setting', name='user_setting'),
    url(r'^signout/$', 'user_logout', name='signout'),
    url(r'^mention/$', 'view_mention', name='mention'),
    url(r'password/$', 'change_password',
        name='change_password'),
    url(r'^avatar/$', 'user_avatar', name='user_avatar'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'reset_confirm', name='password_reset_confirm'),
    url(r'^reset/$', 'reset', name='password_reset'),
    url(r'^reset/password/done/$',
        'password_reset_done',
        name='password_reset_done')
)
