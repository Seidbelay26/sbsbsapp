
from books import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
    
    path('', RedirectView.as_view(url='meetme/')),
    path('meetme/', include('meetme.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)