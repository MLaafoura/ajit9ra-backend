from django.db import models
from Ajit9raLeads.models import Lead


class Communication(models.Model):
    lead = models.ForeignKey(Lead, related_name='communications', on_delete=models.CASCADE, null=True)
    communication_type = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.communication_type} - {self.status}'