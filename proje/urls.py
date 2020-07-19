from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('hmhm/', views.hmhm),
    path('app/', include('app.urls'))
]

urlpatterns += staticfiles_urlpatterns()
