from django.contrib import admin
from websettings.models import Setting

class WebSettingAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)
    fields = ('name','value',)
    list_display = ('name','value',)

    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Setting, WebSettingAdmin)
