from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # URL for hello app
    url(r'^', include('apps.hello.urls')),

)
