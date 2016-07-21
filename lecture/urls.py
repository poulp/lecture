"""lecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.auth.views import logout

from lecture.views import login_lecture, home
from lecture.forms import LectureAuthenticationForm


# login data
login_data = {
    'authentication_form': LectureAuthenticationForm,
}

# logout data
logout_data = {'template_name': 'rest_framework/login.html'}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),

    # api
    url(r'^api/feedroot/', include('lecture.feed.urls')),
    url(r'^api/login/', login_lecture, login_data, name='login'),
    url(r'^api/logout/$', logout, logout_data, name='logout'),
]
