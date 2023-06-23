from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

from .serializers import AccessKeySerializer
from .models import AccessKey


@login_required
def access_keys_list(request):
    if request.user.is_staff:
        access_keys = AccessKey.objects.all()
    else:
        access_keys = AccessKey.objects.filter(user=request.user)
    context = {
        "access_keys": access_keys.order_by("status")
    }
    return render(request, "keys/list.html", context)

@login_required
def request_access_key(request):
    user = request.user
    active_keys = AccessKey.objects.filter(user=user, status="active")

    if active_keys.exists():
        messages.error(request, "A user can have only one active key at a time.")
        return redirect("home")  # Redirect to the access keys list if user has an active key
    
    try:
        new_key = AccessKey(user=user)
        new_key.save()
        messages.success(request, "New Access key successfully generated")
        return redirect("home")
    except Exception as err:
        messages.error(request, str(err))
        return redirect("home")
    

@staff_member_required
@login_required
def revoke_access_key(request, access_key_id):
    access_key = get_object_or_404(AccessKey, pk=access_key_id)

    if access_key.status == "active":
        access_key.status = "revoked"
        access_key.save()
        messages.success(request, f"Key: {access_key.key} successfully revoked")
        return redirect("home")
    messages.error(request, f"Key:{access_key.key} is not active")    
    return redirect("home")

   
# EndPoint
@api_view(["GET"])
@authentication_classes([BasicAuthentication,])
@permission_classes([IsAdminUser,])
def get_active_access_key(request, email):
    try:
        access_key = AccessKey.objects.get(user__email=email, status="active")
        serializer = AccessKeySerializer(access_key)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except AccessKey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)