from django.contrib import admin
from main.models import Setting, RecordType, Domain, ChangePoint

# Register your models here.
admin.site.register(Setting)
admin.site.register(RecordType)
admin.site.register(Domain)
admin.site.register(ChangePoint)