from django.contrib import admin
from .models import Skills
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo)
admin.site.register(Skills)
