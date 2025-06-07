from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    join_date = models.DateField()
    salary=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name}"