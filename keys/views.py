from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import AccessKey
from .forms import AccessKeyRequestForm

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
    active_keys = AccessKey.objects.filter(user=user, status='active')

    if active_keys.exists():
        messages.error(request, "A user can have only one active key at a time.")
        return redirect('home')  # Redirect to the access keys list if user has an active key
    
    try:
        new_key = AccessKey(user=user)
        new_key.save()
        messages.success(request, "New Access key successfully generated")
        return redirect('home')
    except Exception as err:
        messages.error(request,str(err))
        return redirect('home')
