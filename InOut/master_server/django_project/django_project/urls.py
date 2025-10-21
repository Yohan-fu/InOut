from django.urls import path, include

urlpatterns = [
    path("api/", include("master_app.urls")),
]
