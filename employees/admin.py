from django.contrib import admin

from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "position", "employment_date", "salary", "total_paid")
    list_display_links = ("position",)
    list_filter = ("position", "level")
