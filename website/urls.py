from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
	# ex.: index/
	path('', views.index, name='index')
]