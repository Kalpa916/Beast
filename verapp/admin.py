from django.contrib import admin
admin.autodiscover()

# Register your models here.
from .models import StudebtRegistration
class StudebtRegistrationAdmin(admin.ModelAdmin):
    list_display=['id','studentName','studentId','studentClass','StudentGuardiandName','StudentCollegeName','studentPasssword']
admin.site.register(StudebtRegistration,StudebtRegistrationAdmin)
