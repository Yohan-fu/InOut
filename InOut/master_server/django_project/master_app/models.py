from django.db import models

class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100, blank=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    site = models.CharField(max_length=50, default="master_site")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.site})"
