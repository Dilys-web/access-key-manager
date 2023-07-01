from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
openapi.Info(
title="Active Key API",
default_version="v1",
description="Retrieving Active Access Keys",
terms_of_service="Micro-Focus-Inc.com",
contact=openapi.Contact(email="opokudonkord@gmail.com"),
license=openapi.License(name="BSD License"),

),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('keys.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
