from django.db import models
from django.utils.timezone import localdate


class Employee(models.Model):
    """Сотрудники"""
    last_name = models.CharField("Фамилия", max_length=30)
    first_name = models.CharField("Имя", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    position = models.CharField(max_length=100)

    JR = "Jn"
    MD = "Md"
    SR = "Sr"
    DR = "Dr"
    CE = "Ce"
    POSITION_CHOICES = [
        (JR, "Junior"),
        (MD, "Middle"),
        (SR, "Senior"),
        (DR, "Director"),
        (CE, "CEO"),
    ]

    level = models.CharField(max_length=100, choices=POSITION_CHOICES, blank=False, default=JR)
    employment_date = models.DateField("Дата приёма на работу", default=localdate)
    email = models.EmailField('Email', max_length=200, unique=True, default="email@example.com")
    salary = models.DecimalField(
        "Зарплата", max_digits=8, decimal_places=2, default=0, help_text="указывать сумму в долларах"
    )
    total_paid = models.DecimalField(
        "Всего выплачено", max_digits=16, decimal_places=2, default=0, help_text="указывать сумму в долларах"
    )
    is_superuser = models.BooleanField('Superuser', default=False)
    is_staff = models.BooleanField('Staff', default=False)
    # url = models.SlugField(max_length=130, unique=True) не знаю, нужен ли здесь на него урл??


    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
