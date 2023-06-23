import uuid
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import User

def get_default_expiry_date():
    return timezone.now() + timezone.timedelta(days=365)

class AccessKey(models.Model):
    STATUS = [
        ("active", "Active"),
        ("expired", "Expired"),
        ("revoked", "Revoked")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, choices=STATUS, default="active")
    procurement_date = models.DateTimeField(auto_now_add=True)
    # asssuming a key expires after a year
    expiry_date = models.DateTimeField(default=get_default_expiry_date)
    
    class Meta:
        ordering = ["-procurement_date",]
    
    def clean(self, *args, **kwargs):
        # Check if the user already has an active key
        super().clean(*args, **kwargs)
        active_keys = AccessKey.objects.filter(user=self.user, status="active")
        if self.status == "active" and self.pk is None and active_keys.exists():
            raise ValidationError("A user can have only one active key at a time.")

    def __str__(self):
        return str(self.key)