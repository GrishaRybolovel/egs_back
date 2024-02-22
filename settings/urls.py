from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user_app.urls")),
    path("project/", include("project_app.urls")),
    path("task/", include("task_app.urls")),
    path("message/", include("message_app.urls")),
    path("document/", include("document_app.urls")),
    path("mail/", include("mail_app.urls"))
]
