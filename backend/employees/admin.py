from .models import Employee
from django.urls import reverse
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class EmployeeDraggableAdmin(DraggableMPTTAdmin, UserAdmin):
    model = Employee

    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "patronymic",
                           "position", "employment_date", "salary", "total_paid",
                           "head", "is_staff", "is_superuser", "exp")
                }
         ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name",
                       "last_name", "patronymic", "position", "exp", "employment_date",
                       "salary", "total_paid", "head", "is_staff", "is_superuser", )
        }
         ),
    )

    ordering = ("level",)
    list_display = ("tree_actions", "get_full_name",
                    "position", "salary", "total_paid",
                    "link_to_head", "exp",
                    )
    list_display_links = ["get_full_name", "link_to_head"]
    list_filter = ("position", "level")
    actions = ["delete_payment_info"]

    def link_to_head(self, obj):
        link = reverse("admin:employees_employee_change", args=[obj.head_id])
        if not obj.head:
            return format_html("<span> No head </span>", link, obj.head)
        return format_html("<a href="{}">{}</a>", link, obj.head)

    link_to_head.short_description = "Head"
    link_to_head.allow_tags = True


admin.site.register(Employee, EmployeeDraggableAdmin)