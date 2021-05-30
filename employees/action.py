from employees.models import Employee


def delete_total_paid(queryset):
    for paid in queryset:
        paid = Employee.objects.get(pk=paid)
        paid.total_paid = 0
        paid.save()
