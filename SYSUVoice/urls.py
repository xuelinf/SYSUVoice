from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import forum
from SYSUVoice import settings

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('forum.urls')),
                       url(r'^user/', include('account.urls')),
                       url(r'^api/forum/',
                           include(forum.urls.api_urlpatterns)),
                       url(r'^manage/', include('panel.urls',
                           namespace='panel', app_name='panel')),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
