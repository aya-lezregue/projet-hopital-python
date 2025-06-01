from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accueil
    path('', home, name='home'),  

    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Application principale
    path('core/', include('core.urls')),

]
