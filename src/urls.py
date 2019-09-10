"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


# defining a custom 404 error view here so we can customize as needed
# also so we can view in development, with '404' route below
def error404(request, exception=None):
    return render(request, '404.html', status=404)


# overrides default 404 view with our custom one
handler404 = error404

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),

    # http://staticfiles.productiondjango.com/blog/failproof-favicons/
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    # path('apple-touch-icon-precomposed.png', RedirectView.as_view(url=staticfiles_storage.url('images/apple-touch-icon.png'))),
    # path('apple-touch-icon.png', RedirectView.as_view(url=staticfiles_storage.url('images/apple-touch-icon.png'))),
    # path('404/', error404, name='404'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
