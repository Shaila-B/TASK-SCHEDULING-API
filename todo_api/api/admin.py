from django.contrib import admin
from .models import Task, Organization

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignee', 'status', 'create_at', 'update_at')
    list_filter = ('status', 'create_at', 'update_at')
    search_fields = ('assignee', 'title')
    list_editable = ('status',)
    date_hierarchy = ('create_at')
 

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Task, TaskAdmin)