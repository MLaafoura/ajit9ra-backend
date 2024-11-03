from django.db import models


class Programs(models.Model):
    university_name = models.CharField(max_length=1000)
    program_name = models.CharField(max_length=1000)
    university_location = models.CharField(max_length=255)
    program_description = models.CharField(max_length=1000)
    program_image = models.ImageField(upload_to='media/Program/Images')