from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include(("shop.urls", "shop"), namespace="shop")),
    path("account/", include(("account.urls", "account"), namespace="account"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
