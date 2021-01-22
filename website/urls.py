from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
	# ex.: index/
	path('', views.index, name='index'),
	# ex.: index/4
	path('<int:livro_id>', views.detail, name='detail'),
	# ex.: index/search/?term=?
	path('search/', views.search, name='search'),
]