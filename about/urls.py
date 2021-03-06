from django.conf.urls import url

from about import views

urlpatterns = [
    # Matches http://example.com/about
    url(r'^$', views.index, name='index'),

    # Matches http://example.com/about/dnollk
    url(r'^dnollk/$', views.dnollk, name="dnollk"),

    # Matches http://example.com/about/foreningar
    url(r'^sektionen/$', views.sektionen, name="sektionen"),

    url(r'^brage/$', views.brage, name="brage"),

    url(r'^donk/$', views.donk, name="donk"),
]
