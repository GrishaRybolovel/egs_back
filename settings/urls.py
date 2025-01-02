from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path("v1/schema/docs", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("admin/", admin.site.urls),
    path("user/", include("user_app.urls")),
    path("project/", include("project_app.urls")),
    path("task/", include("task_app.urls")),
    path("message/", include("message_app.urls")),
    path("document/", include("document_app.urls")),
    path("mail/", include("mail_app.urls"))
]
