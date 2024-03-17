from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_laboratory_assistant = models.BooleanField(default=False)

    # Добавляем аргумент related_name для обратных связей с группами и разрешениями пользователя
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.username

class AnalysisResult(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    result = models.TextField()

    def __str__(self):
        return f"Result for {self.patient} on {self.date}"
