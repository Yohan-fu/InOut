from django.urls import path, include

urlpatterns = [
    path("api/", include("child_app.urls")),
]
