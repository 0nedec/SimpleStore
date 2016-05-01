from django.conf.urls import patterns, include, url
import views

urlpatterns = [
    url(r'^$', views.catalog, name = "catalog" ),
]