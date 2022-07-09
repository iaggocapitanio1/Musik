from django.urls import path, include

from .views import RoomView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("home", RoomView.as_view())
]
