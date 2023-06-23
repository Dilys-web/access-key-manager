from django.contrib import admin
from .models import AccessKey

class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ("key", "status", "procurement_date", "expiry_date", "user")
    list_filter = ("status", "user")
    search_fields = ("key",)
    readonly_fields = ("key", "procurement_date", "expiry_date")
    actions = ["mark_as_expired", "mark_as_revoked", "mark_as_active"]

    def mark_as_expired(self, request, queryset):
        queryset.update(status="expired")

    def mark_as_revoked(self, request, queryset):
        queryset.update(status="revoked")

    mark_as_expired.short_description = "Mark selected access keys as expired"
    mark_as_revoked.short_description = "Mark selected access keys as revoked"
    mark_as_active.short_description = "Mark selected access keys as active"

admin.site.register(AccessKey, AccessKeyAdmin)
