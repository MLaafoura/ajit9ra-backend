from django.db.models.signals import post_save
from django.dispatch import receiver
from Ajit9raLeads.models import Lead
from .models import Communication

@receiver(post_save, sender=Lead)
def create_communication(sender, instance, created, **kwargs):
    if not created:
        Communication.objects.create(
            lead = instance,
            Communication_type = instance.communication_type,
            status = instance.lead_status,
            note = instance.note

        )