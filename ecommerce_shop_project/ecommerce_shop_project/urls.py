from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    #path("", RedirectView.as_view(url="admin/", permanent=False), name="index"),
    path("", include("shop.urls"))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
