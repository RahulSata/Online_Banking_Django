"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from loginmodule.views import login,auth_view,logout,loggedin,invalidlogin,transaction,do_transaction,display,profile,loan,home,need_help,about_us,changepw,changedb
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^home/$',home),
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
	url(r'^logout/$', logout),
	url(r'^loggedin/$', loggedin),
	url(r'^invalidlogin/$', invalidlogin),
	url(r'^transaction/$', transaction),
    url(r'^do_transaction/$',do_transaction),
    url(r'^display/$',display),
    url(r'^profile/$',profile),
    url(r'^loan/$',loan),
    url(r'^need_help/$',need_help),
    url(r'^about_us/$',about_us),
    url(r'^changepw/$',changepw),
    url(r'^changedb/$',changedb),
]
