from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UtilisateurCreationForm
from django.urls import reverse_lazy
from .models import Patient, Medecin, Facture, DossierMedical
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from .models import RendezVous
from .models import Consultation
from .forms import RendezVousForm
from .forms import ConsultationForm
from .forms import DossierMedicalForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import (
    Patient, Medecin, RendezVous,
    Consultation, DossierMedical, Facture
)
from .forms import (
    PatientForm, MedecinForm, RendezVousForm,
    ConsultationForm, DossierMedicalForm, FactureForm
)
from django.contrib.auth.forms import UserCreationForm


# ---------- Patient Views ----------
class PatientList(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'

class PatientDetail(DetailView):
    model = Patient
    template_name = 'patients/detail.html'
    context_object_name = 'patient'

class PatientCreate(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdate(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'patients/confirm_delete.html'
    success_url = reverse_lazy('patient_list')


# ---------- Médecin Views ----------
class MedecinList(ListView):
    model = Medecin
    template_name = 'medecins/list.html'
    context_object_name = 'medecins'

class MedecinDetail(DetailView):
    model = Medecin
    template_name = 'medecins/detail.html'
    context_object_name = 'medecin'

class MedecinCreate(CreateView):
    model = Medecin
    form_class = MedecinForm
    template_name = 'medecins/form.html'
    success_url = reverse_lazy('medecin_list')

class MedecinUpdate(UpdateView):
    model = Medecin
    form_class = MedecinForm
    template_name = 'medecins/form.html'
    success_url = reverse_lazy('medecin_list')

class MedecinDelete(DeleteView):
    model = Medecin
    template_name = 'medecins/confirm_delete.html'
    success_url = reverse_lazy('medecin_list')


# ---------- RendezVous Views ----------
class RendezVousList(ListView):
    model = RendezVous
    template_name = 'rendezvous/list.html'
    context_object_name = 'rendezvous_list'

class RendezVousDetail(DetailView):
    model = RendezVous
    template_name = 'rendezvous/detail.html'
    context_object_name = 'rendezvous'

class RendezVousCreate(CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'rendezvous/form.html'
    success_url = reverse_lazy('rdv_list')

class RendezVousUpdate(UpdateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'rendezvous/form.html'
    success_url = reverse_lazy('rdv_list')

class RendezVousDelete(DeleteView):
    model = RendezVous
    template_name = 'rendezvous/confirm_delete.html'
    success_url = reverse_lazy('rdv_list')


# ---------- Consultation Views ----------
class ConsultationList(ListView):
    model = Consultation
    template_name = 'consultations/list.html'
    context_object_name = 'consultations'

class ConsultationDetail(DetailView):
    model = Consultation
    template_name = 'consultations/detail.html'
    context_object_name = 'consultation'

class ConsultationCreate(CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultations/form.html'
    success_url = reverse_lazy('consultation_list')

class ConsultationUpdate(UpdateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultations/form.html'
    success_url = reverse_lazy('consultation_list')

class ConsultationDelete(DeleteView):
    model = Consultation
    template_name = 'consultations/confirm_delete.html'
    success_url = reverse_lazy('consultation_list')


# ---------- DossierMedical Views ----------
class DossierMedicalList(ListView):
    model = DossierMedical
    template_name = 'dossiers/list.html'
    context_object_name = 'dossiers'

class DossierMedicalDetail(DetailView):
    model = DossierMedical
    template_name = 'dossiers/detail.html'
    context_object_name = 'dossier'

class DossierMedicalCreate(CreateView):
    model = DossierMedical
    form_class = DossierMedicalForm
    template_name = 'dossiers/form.html'
    success_url = reverse_lazy('dossier_list')

class DossierMedicalUpdate(UpdateView):
    model = DossierMedical
    form_class = DossierMedicalForm
    template_name = 'dossiers/form.html'
    success_url = reverse_lazy('dossier_list')

class DossierMedicalDelete(DeleteView):
    model = DossierMedical
    template_name = 'dossiers/confirm_delete.html'
    success_url = reverse_lazy('dossier_list')


# ---------- Facture Views ----------
class FactureList(LoginRequiredMixin, ListView):
    model = Facture
    template_name = 'factures/list.html'
    context_object_name = 'factures'

    def get_queryset(self):
        # Si l'utilisateur est un patient, on affiche ses factures
        user = self.request.user
        if hasattr(user, 'patient'):
            return Facture.objects.filter(patient=user)
        # Sinon on retourne rien (ou tout si admin/médecin)
        return Facture.objects.none()

class FactureDetail(DetailView):
    model = Facture
    template_name = 'factures/detail.html'
    context_object_name = 'facture'

class FactureCreate(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/form.html'
    success_url = reverse_lazy('facture_list')

class FactureUpdate(UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/form.html'
    success_url = reverse_lazy('facture_list')

class FactureDelete(DeleteView):
    model = Facture
    template_name = 'factures/confirm_delete.html'
    success_url = reverse_lazy('facture_list')


# ---------- User Registration View ----------


def signup(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            return redirect('home')  # À adapter selon ta page d'accueil
    else:
        form = UtilisateurCreationForm()
    return render(request, 'core/signup.html', {'form': form})
def home(request):
    return render(request, 'core/home.html')
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)

        # Vérifie d'abord si l'utilisateur est un patient
        try:
            patient = Patient.objects.get(pk=user.pk)
            return redirect('dashboard_patient')  # Redirige vers la page des spécialités
        except Patient.DoesNotExist:
            pass

        # Vérifie s'il est médecin
        if Medecin.objects.filter(pk=user.pk).exists():
            return redirect('medecin_dashboard')

        # Vérifie s'il est admin
        if user.is_superuser:
            return redirect('/admin/')

        # Fallback
        return redirect('home')

    return render(request, 'core/login.html', {'form': form})

@login_required
def specialites_view(request):
    specialites = [
        'Cardiologie',
        'Dermatologie',
        'Pédiatrie',
        'Gynécologie',
        'Ophtalmologie',
        'Neurologie',
        'Psychiatrie',
        'Orthopédie',
        'ORL (Oto-Rhino-Laryngologie)',
        'Endocrinologie',
        'Urologie',
        'Gastroentérologie',
        'Pneumologie',
        'Rhumatologie',
    ]
    return render(request, 'core/specialites.html', {'specialites': specialites})

    
def medecins_par_specialite(request, specialite):
    medecins = Medecin.objects.filter(specialite=specialite)
    return render(request, 'core/filtre_par_specialite.html', {
        'specialite': specialite,
        'medecins': medecins
    })


def fiche_medecin(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    return render(request, 'core/fiche_medecin.html', {'medecin': medecin})

@login_required
def prendre_rendez_vous(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)

    # Assure-toi que l'utilisateur est un patient
    try:
        patient = Patient.objects.get(pk=request.user.pk)
    except Patient.DoesNotExist:
        return redirect('home')  # Ou afficher un message d'erreur

    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.medecin = medecin
            rdv.patient = patient
            rdv.save()
            return redirect('specialites')  # Rediriger vers confirmation ou autre
    else:
        form = RendezVousForm()

    return render(request, 'core/prendre_rendez_vous.html', {'form': form, 'medecin': medecin})

@login_required
def dashboard_patient(request):
    """
    Vue qui affiche le tableau de bord pour l'utilisateur connecté,
    s'il s'agit d'un patient.
    """
    # Étape 1 : Récupérer l'utilisateur connecté
    user = request.user

    try:
        # Étape 2 : Récupérer l'objet Patient lié à cet utilisateur
        patient = Patient.objects.get(pk=user.pk)
    except Patient.DoesNotExist:
        # Si l'utilisateur n'est pas un patient, on le redirige vers l'accueil
        return redirect('home')

    # Étape 3 : Préparer le contexte à envoyer au template
    context = {
        'patient': patient
    }

    # Étape 4 : Rendu de la page dashboard avec les données du patient
    return render(request, 'core/dashboard.html', context)

@login_required
def mes_rendezvous(request):
    # Exemple simple, à adapter
    patient = Patient.objects.get(pk=request.user.pk)
    rendezvous = RendezVous.objects.filter(patient=patient)
    return render(request, 'core/mes_rendezvous.html', {'rendezvous': rendezvous})

@login_required
def mes_factures(request):
    print("Utilisateur connecté :", request.user)

    try:
        patient = request.user.patient
        print("Patient récupéré :", patient)
    except Exception as e:
        print("Erreur :", e)
        messages.error(request, "Vous devez être connecté en tant que patient pour voir vos factures.")
        return redirect('home')

    factures = Facture.objects.filter(patient=patient)
    print("Factures trouvées :", factures)

    return render(request, 'core/mes_factures.html', {'factures': factures})



@login_required
def mon_dossier_medical(request):
    try:
        patient = request.user.patient
    except:
        messages.error(request, "Vous devez être connecté en tant que patient pour accéder à cette page.")
        return redirect('home')

    # Trouver tous les dossiers médicaux liés à ce patient via les consultations
    dossiers = DossierMedical.objects.filter(consultations__rendezvous__patient=patient).distinct()

    return render(request, 'core/visualiser_dossiers.html', {'dossiers': dossiers})



@login_required
def visualiser_rendezvous_view(request):
    try:
        medecin = request.user.medecin
    except:
        return redirect('home')  # ou afficher un message

    rendezvous = RendezVous.objects.filter(medecin=medecin).order_by('-date')
    return render(request, 'core/visualiser_rendezvous.html', {'rendezvous': rendezvous})

def creer_dossier_medical(request):
    selected_patient = None

    if request.method == 'POST':
        selected_patient_id = request.POST.get('patient')
        selected_patient = Patient.objects.get(id=selected_patient_id)
        form = DossierMedicalForm(request.POST, patient=selected_patient)
        if form.is_valid():
            form.save()
            return redirect('medecin_dashboard')
            
    else:
        selected_patient_id = request.GET.get('patient')
        if selected_patient_id:
            selected_patient = Patient.objects.get(id=selected_patient_id)
            form = DossierMedicalForm(patient=selected_patient)
        else:
            form = None

    patients = Patient.objects.all()
    return render(request, 'core/creer_dossier.html', {
        'form': form,
        'patients': patients,
        'selected_patient': selected_patient
    })

@login_required
def medecin_dashboard(request):
       return render(request, 'core/dashboard_medecin.html')

@login_required
def creer_consultation_view(request):
    medecin = request.user.medecin

    if request.method == 'POST':
        form = ConsultationForm(request.POST, medecin=medecin)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.medecin = medecin
            consultation.save()
            return redirect('visualiser_consultations')
    else:
        form = ConsultationForm(medecin=medecin)

    return render(request, 'core/creer_consultation.html', {'form': form})


@login_required
def visualiser_consultations_view(request):
    try:
        medecin = request.user.medecin
    except:
        return redirect('home')

    consultations = Consultation.objects.filter(
        rendezvous__medecin=medecin
    ).order_by('-rendezvous__date')

    return render(request, 'core/visualiser_consultations.html', {
        'consultations': consultations
    })

@login_required
def visualiser_dossiers_view(request):
    dossiers = DossierMedical.objects.all()
    return render(request, 'core/visualiser_dossiers.html', {'dossiers': dossiers})

@login_required
def mes_rendezvous(request):
    try:
        patient = request.user.patient
    except:
        messages.error(request, "Vous devez être connecté en tant que patient pour voir vos rendez-vous.")
        return redirect('home')

    rendezvous = RendezVous.objects.filter(patient=patient)
    return render(request, 'core/visualiser_rendezvous.html', {'rendezvous': rendezvous})
