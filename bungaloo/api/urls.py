from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import ListView

urlpatterns = {
    url(r'^homes/$', ListView.as_view(), name="homes"),
    url(r'^homes/create$', CreateView.as_view(), name="create"),
    url(r'^homes/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)