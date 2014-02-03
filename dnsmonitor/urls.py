from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='main/table.html', permanent=False), name='index'),
    url(r'^home', 'main.views.home', name='home'),
    url(r'^main/table.html', 'main.views.table', name="table"),
    url(r'^main/item.html/(\d+)/(\d+)/$', 'main.views.item', name="item"),

    url(r'^admin/', include(admin.site.urls)),
)
