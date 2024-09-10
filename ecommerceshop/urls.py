from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from wkhtmltopdf.views import PDFTemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    path("cart/", include("carts.urls")),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
    path("chat/", include("chat.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
