from django.db import models
from django.contrib.auth.models import AbstractUser

# Constantes pour les choix
GENRE_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin'),
]

# Modèle de base utilisateur
class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    cin = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

    def __str__(self):
        return f"{self.username}"

# Patient hérite d'Utilisateur
class Patient(Utilisateur):
    raison_consultation = models.CharField(max_length=255)
    visite = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.username} - Patient"

# Médecin hérite d'Utilisateur
class Medecin(Utilisateur):
    specialite = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Médecin"
        verbose_name_plural = "Médecins"

    def __str__(self):
        return f"Dr. {self.username} - {self.specialite}"

# Admin hérite d'Utilisateur via un proxy
class Admin(Utilisateur):
    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.username} - Admin"

# Rendez-vous entre patient et médecin
class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"RDV {self.date} à {self.heure} - {self.patient.username} avec {self.medecin.username}"

# Consultation liée à un rendez-vous
class Consultation(models.Model):
    rendezvous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)
    diagnostic = models.TextField()
    traitement_prescrit = models.TextField()
    duree = models.DurationField()
    medicament = models.CharField(max_length=255)

    def __str__(self):
        return f"Consultation - {self.rendezvous}"

# Dossier médical d'une consultation
class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True, blank=True)
    consultations = models.ManyToManyField('Consultation')
    groupe_sanguin = models.CharField(max_length=5)
    alergie = models.TextField()
    maladie_chronique = models.TextField()

    def __str__(self):
        if self.patient:
            return f"Dossier de {self.patient.username}"
        else:
            return "Dossier (patient non défini)"

# Facture liée à une consultation
class Facture(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_fact = models.DateField()
    montant_tot = models.DecimalField(max_digits=10, decimal_places=2, default=300.00)

    def save(self, *args, **kwargs):
        self.montant_tot = 300.00  # force 300 dh peu importe
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Facture de {self.patient.username} - {self.date_fact} - {self.montant_tot} MAD"
