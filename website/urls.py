from django.views.generic import RedirectView

from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', RedirectView.as_view(url='https://github.com/Ahlat85')),
  path('github/', include('apps.github.urls')),
]