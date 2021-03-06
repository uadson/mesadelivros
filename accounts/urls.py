from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
	path('', views.login, name='index_login'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('cadlivro/', views.cadlivro, name='cadlivro'),
	path('cadcateg/', views.cadcateg, name='cadcateg'),
	path('pwreset/', views.pwreset, name='pwreset'),
	path('pwreset/confirm/', views.pwreset, name='pwconfirm'),

	path('user/', views.user, name='userform'),
]