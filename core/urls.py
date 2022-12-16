from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.accounts.views import (
    login, logout, pwreset, register, dashboard, user
)

from apps.books.views import (
    index, detail, search, cadcateg, cadlivro, altlivro, del_livro
)

app_name = [
    'accounts', 'books'
]

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # accounts app
    path('accounts/', login, name='index_login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('pwreset/', pwreset, name='pwreset'),
    path('pwreset/confirm/', pwreset, name='pwconfirm'),
    path('user/', user, name='userform'),
    
    # books app
    path('', index, name='index'),
    path('detalhe/<int:livro_id>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('cadlivro/', cadlivro, name='cadlivro'),
	path('cadcateg/', cadcateg, name='cadcateg'),
    path('alterar/<int:pk>/', altlivro, name='altlivro'),
    path('excluir/<int:pk>/', del_livro, name='del_livro'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
