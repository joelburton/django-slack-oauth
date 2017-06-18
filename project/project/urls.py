"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cats import views

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^cats/$', views.CatListView.as_view(), name='cat_list'),
    url(r'^cats/(?P<pk>\d+)/$', views.CatDetailView.as_view(), name='cat_detail'),
    url(r'^cats/(?P<pk>\d+)/-edit/$', views.CatUpdateView.as_view()),
    url(r'^cats/-add/$', views.CatCreateView.as_view()),
    url(r'^tweet/$', views.TweetView.as_view()),
    
]
