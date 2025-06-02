from django.db import models

# Create your models here.
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True, auto_created=True)
    deptname = models.CharField(max_length=50)

    def __str__(self):
        return self.deptname

