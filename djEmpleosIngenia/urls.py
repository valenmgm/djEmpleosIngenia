"""djEmpleosIngenia URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from home import viewsH
from vacantes import viewsV
from contacto import viewsC

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', viewsH.renderHome, name='urlHome'),
    url(r'^infoingenia/$', viewsH.renderIngeniaInfo, name='urlInfoIngenia'),
    url(r'^beneficios/$', viewsH.renderBeneficios, name='urlBeneficios'),
    url(r'^vacantes/$', viewsV.renderVacantes, name='urlVacantes'),
    url(r'^contacto/$', viewsC.renderContactoIngenia, name='urlContacto'),
    url(r'^aplicaya/$', viewsC.renderAplicaYa, name='urlAplicaYa')
]
