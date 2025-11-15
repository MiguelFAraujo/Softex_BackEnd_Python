from django.contrib import admin 
from django.urls import path, include 
# 1. Importe as views de autenticação 
from django.contrib.auth import views as auth_views 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('core.urls')), # Nossas URLs do app 'core' 
     
    # 2. ADICIONE ESTAS URLs 
     
    # URL de Login 
    # Ela usa a View pronta 'LoginView' e diz a ela para usar nosso template 
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'),  name='login'), 
          
    # URL de Logout 
    # Ela usa a View 'LogoutView'. 'next_page' diz para onde ir após o logout. 
    path('logout/',  auth_views.LogoutView.as_view(next_page='login'),  name='logout'), 
] 