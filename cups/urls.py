from django.conf.urls import patterns, url
from cups import views

urlpatterns = patterns('',
	url(r'^add/?',views.add_cup,name='add'),
	)