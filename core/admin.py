from django.contrib import admin
from .models import Enter, Order, WorkerProduct
# Register your models here.
from users.models import User


class WorkerProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "worker":
            kwargs["queryset"] = User.objects.filter(user_roles='worker')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(WorkerProduct, WorkerProductAdmin)
admin.site.register(Enter)
admin.site.register(Order)
