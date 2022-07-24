from django.db import models

# Create your models here.
class Task1(models.Model):

    task_ref_no=models.IntegerField()
    instruction=models.CharField(max_length=100)
    file=models.FileField(upload_to='file',blank=True,null=True)
