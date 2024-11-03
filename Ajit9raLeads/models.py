from django.db import models


class Lead(models.Model):
    LEAD_STATUS_CHOICES = [
        ('new', 'New'),
        ('no_answer_1', 'No Answer 1'),
        ('no_answer_2', 'No Answer 2'),
        ('no_answer_3', 'No Answer 3'),
        ('in_progress', 'In Progress'),
        ('not_interested', 'Not Interested'),
        ('invalid', 'Invalid'),
    ]

    LEAD_QUALITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('graduated_graduating', 'Graduated / Graduating'),
        ('future_candidate', 'Future Candidate'),
    ]

    COMMUNICATION_TYPE_CHOICES = [
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('call', 'Call'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    lead_status = models.CharField(
        max_length=20,
        choices=LEAD_STATUS_CHOICES,
        default='new'
    )

    lead_quality = models.CharField(
        max_length=10,
        choices=LEAD_QUALITY_CHOICES,
        default='medium'
    )

    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVEL_CHOICES,
        default='graduated_graduating'
    )

    communication_type = models.CharField(
        max_length=10,
        choices=COMMUNICATION_TYPE_CHOICES,
        default='email'
    )

    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
