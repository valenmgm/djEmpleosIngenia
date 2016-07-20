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

from django.conf import settings
from django.conf.urls.static import static

from homeApp import viewsH
from ingeniaApp import viewsI
from vacantesApp import viewsV
from contactoApp import viewsC
from beneficiosApp import viewsB

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', viewsH.renderHome, name='urlHome'),
    url(r'^ingenia/$', viewsI.renderIngenia, name='urlIngenia'),
    url(r'^beneficios/$', viewsB.renderBeneficios, name='urlBeneficios'),
    url(r'^vacantes/$', viewsV.renderVacantes, name='urlVacantes'),
    url(r'^contacto/$', viewsC.renderContactoIngenia, name='urlContacto'),
    url(r'^exito/$', viewsC.renderExito, name='urlExito'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
