"""ndevlopi URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from course import views
from contact import views as contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/',contact_view.contact),
    url(r'^(?P<slug>[-\w]+)/$', views.DetailCourse.as_view(),name="course"),
    url(r'^(?P<slug>[-\w]+)/(?P<chpiter_slug>[-\w]+)-(?P<pk>[0-9]{2})/$', views.detail_video,name="video"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


