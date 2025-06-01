from django import forms
from .models import Consultation, RendezVous
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    Utilisateur,
    Patient,
    Medecin,
    RendezVous,
    Consultation,
    DossierMedical,
    Facture
)

# ----- Formulaire d'inscription pour Patient uniquement -----
class UtilisateurCreationForm(UserCreationForm):
    raison_consultation = forms.CharField(
        required=True, 
        label="Raison de visite"
    )
    visite = forms.BooleanField(
        required=False,
        label="A-t-il déjà visité l'hôpital ?"
    )

    class Meta:
        model = Utilisateur
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'telephone', 'adresse', 'cin', 'ville', 'genre'
        ]

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        if commit:
            utilisateur.save()

            Patient.objects.create(
                id=utilisateur.id,
                username=utilisateur.username,
                password=utilisateur.password,
                first_name=utilisateur.first_name,
                last_name=utilisateur.last_name,
                email=utilisateur.email,
                telephone=utilisateur.telephone,
                adresse=utilisateur.adresse,
                cin=utilisateur.cin,
                ville=utilisateur.ville,
                genre=utilisateur.genre,
                raison_consultation=self.cleaned_data.get('raison_consultation'),
                visite=self.cleaned_data.get('visite') or False
            )

        return utilisateur


# ----- Formulaire d'administration : modification utilisateur -----
class UtilisateurChangeForm(UserChangeForm):
    class Meta:
        model = Utilisateur
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'telephone', 'adresse', 'cin', 'ville',
            'genre'
        ]


# ----- Formulaires classiques pour les modèles -----

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'

class RendezVousForm(forms.ModelForm):
     class Meta:
        model = RendezVous
        exclude = ['patient', 'medecin']
        fields = ['patient', 'medecin', 'date', 'heure']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure': forms.TimeInput(attrs={'type': 'time'}),
        }


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['rendezvous', 'diagnostic', 'traitement_prescrit', 'duree', 'medicament']
        widgets = {
            'duree': forms.TextInput(attrs={'placeholder': 'Ex: 1:30:00 pour 1h30'}),
        }

    def __init__(self, *args, **kwargs):
        self.medecin = kwargs.pop('medecin', None)  # récupère le médecin
        super().__init__(*args, **kwargs)

        if self.medecin:
            self.fields['rendezvous'].queryset = RendezVous.objects.filter(medecin=self.medecin)

    def save(self, commit=True):
        consultation = super().save(commit=commit)

        # Création automatique de la facture
        if commit:
            patient = consultation.rendezvous.patient
            montant_par_defaut = 200  # Tu peux modifier ce montant selon ta logique

            Facture.objects.create(
                patient=patient,
                consultation=consultation,
                montant_tot=montant_par_defaut
            )

        return consultation

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = ['consultations', 'groupe_sanguin', 'alergie', 'maladie_chronique']

    def __init__(self, *args, **kwargs):
        patient = kwargs.pop('patient', None)
        super().__init__(*args, **kwargs)
        if patient:
            self.fields['consultations'].queryset = Consultation.objects.filter(rendezvous__patient=patient)
        else:
            self.fields['consultations'].queryset = Consultation.objects.none()


class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['patient', 'consultation', 'date_fact', 'montant_tot']
        widgets = {
            'date_fact': forms.DateInput(attrs={'type': 'date'}),
        }
