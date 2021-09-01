"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
    path('LeeshaLarsenGarments', views.LeeshaLarsenGarments, name='LeeshaLarsenGarments'),
    # path('removepunc',views.removepunc,name='rempun'),
    # path('Newlineremover',views.Newlineremover,name='Newlineremover'),
    path('home',views.home,name='home'),
    # path('ex1', views.ex1, name='ex1'),
    path('GABRIALFURNITURE', views.GABRIALFURNITURE, name="GABRIALFURNITURE"),
    path('ContactAldron',views.ContactAldron, name="ContactAldron"),
    path('DigitalPrinting',views.DigitalPrinting,name="DigitalPrinting"),
    path('ContactRajath',views.ContactRajath,name="ContactRajath"),
    path("",views.GABRIALFURNITURE,name="zir.jpeg"),
    path("",views.index,name="julianacomplex.jpeg"),
    path("",views.DigitalPrinting,name="printer.jpeg"),
    path("",views.LeeshaLarsenGarments,name="dress.jpeg"),
    path("",views.LeeshaLarsenGarments,name="dress back.jpeg"),
    path("",views.LeeshaLarsenGarments,name="dress price.jpeg"),
    path("",views.LeeshaLarsenGarments,name="dresstrial.jpeg"),
    path("contactus",views.contactus,name="contactus.html"),
    path("",views.GABRIALFURNITURE,name="furniture.jpeg"),
    path("",views.index,name="julianacomhome.jpeg"),
    path("chickenshop",views.chickenshop,name="chickenshop.html"),
    path('ContactKrishna',views.ContactKrishna, name='ContactKrishna.html'),

]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
