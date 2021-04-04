from django.contrib import admin
from . import models
from .models import Books, ApplicationStatus, Clients, Request, ClearanceStatus, Employee, Formalization


admin.site.register(Books)
admin.site.register(ApplicationStatus)
admin.site.register(Clients)
admin.site.register(Request)
admin.site.register(ClearanceStatus)
admin.site.register(Employee)
admin.site.register(Formalization)


# @admin.register(models.Clients)
# class TypeAdmin(admin.ModelAdmin):
#     pass
