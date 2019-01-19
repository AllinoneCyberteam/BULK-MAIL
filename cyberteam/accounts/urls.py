from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'accounts'


urlpatterns = [
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^email/$', views.email_view, name="email"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout")
]