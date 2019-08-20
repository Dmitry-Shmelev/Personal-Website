from django.contrib import admin

from .models import UserInfo, LatestProject

# Register your models here.


class LatestProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'summary', 'image', 'image_preview','description', 'project_URL', 'pub_date', )
    readonly_fields = ('image_preview', )


admin.site.register(UserInfo)
admin.site.register(LatestProject, LatestProjectAdmin)
