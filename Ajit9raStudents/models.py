from django.db import models


GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    student_picture = models.FileField(upload_to='Students/Picturs/', null=True)
    passport_id_number = models.CharField(max_length=100, null=True)
    issue_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    passport_id_picture = models.FileField(upload_to='Students/Documents/', null=True)
    last_institution_name = models.CharField(max_length=255, null=True)
    original_diploma = models.FileField(upload_to='Student/Education/Documents/Original/Diploma/', null=True)
    translated_diploma = models.FileField(upload_to='Student/Education/Documents/Translated/Diploma/', null=True)
    original_transcript = models.FileField(upload_to='Student/Education/Documents/Original/Transcript/', null=True)
    translated_transcript = models.FileField(upload_to='Student/Education/Documents/Translated/Transcript/', null=True)