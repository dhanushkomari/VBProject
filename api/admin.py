from django.contrib import admin
from . models import VersionSetting, Voice

# Register your models here.

admin.site.register(Voice)
admin.site.register(VersionSetting)
