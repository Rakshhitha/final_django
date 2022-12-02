from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table="department"
