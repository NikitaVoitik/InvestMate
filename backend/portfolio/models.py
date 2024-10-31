from django.db import models
from users.models import User


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}, {self.user.email}"

