from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consultation, Facture

@receiver(post_save, sender=Consultation)
def creer_facture_automatique(sender, instance, created, **kwargs):
    if created:
        patient = instance.rendezvous.patient
        Facture.objects.create(
            patient=patient,
            consultation=instance,
            date_fact=instance.rendezvous.date  # ou timezone.now().date()
        )
