from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("cart", include("cart.urls")),
    path("contact/", include("contact.urls")),
    path("", include(("shop.urls", "shop"), namespace="shop")),
    path("account/", include(("account.urls", "account"), namespace="account")),
    path("staff/", include(("staff.urls", "staff"), namespace="staff")),
    path('orders/', include('orders.urls')),
    path('dynamic_cart/', include("dynamic_cart.urls")),
    path('subscription/', include('subscription.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
