from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('nessus/', include('Nessus_Parser.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.login_user, name='login'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
