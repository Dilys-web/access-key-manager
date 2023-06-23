from django.urls import path
from . import views

urlpatterns = [
    path("", views.access_keys_list, name="home"),
    path("new-key/", views.request_access_key, name="new_key"),
    path("revoke-key/<int:access_key_id>/", views.revoke_access_key, name="revoke_key"),
    path("api/access-keys/<str:email>/", views.get_active_access_key, name="active_access_key"),
]
