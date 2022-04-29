from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

r = DefaultRouter()
r.register('muallif', MuallifViewSet)
r.register('maqola', MaqolaViewSet)
r.register('talks', TalksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls)),
    path('token-ber/', TokenObtainPairView.as_view()),
    path('token-yangila/', TokenRefreshView.as_view()),
]
