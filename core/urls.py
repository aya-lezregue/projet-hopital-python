from . import views
from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views
from .views import mon_dossier_medical, mes_rendezvous, creer_dossier_medical



urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Authentification
    path('signup/', views.signup, name='signup'),

    path('login/', views.login_view, name='login'),

    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),

    path('mes-rendezvous/', views.mes_rendezvous, name='mes_rendezvous'),

    path('mon-dossier-medical/', views.mon_dossier_medical, name='mon_dossier_medical'),
    
    path('specialites/', views.specialites_view, name='specialites'),

    path('mes-factures/', views.mes_factures, name='mes_factures'),
    
    path('medecins/<int:pk>/', views.fiche_medecin, name='fiche_medecin'),

    path('medecin/<int:medecin_id>/rendez-vous/', views.prendre_rendez_vous, name='prendre_rendez_vous'),

    path('medecins/specialite/<str:specialite>/', views.medecins_par_specialite, name='medecins_par_specialite'),

    path('dashboard/medecin/', views.medecin_dashboard, name='medecin_dashboard'),

    path('creer-dossier/', views.creer_dossier_medical, name='creer_dossier_medical'),

    path('medecin/rendezvous/', views.visualiser_rendezvous_view, name='visualiser_rendezvous'),

    path('medecin/dossiers/', views.visualiser_dossiers_view, name='visualiser_dossiers'),

    path('medecin/consultation/creer/', views.creer_consultation_view, name='creer_consultation'),

    path('medecin/consultations/', views.visualiser_consultations_view, name='visualiser_consultations'),

    path('mon-dossier-medical/', mon_dossier_medical, name='mon_dossier_medical'),

    path('mes-rendezvous/', mes_rendezvous, name='mes_rendezvous'),
   


    # Patients
    path('patients/',                     views.PatientList.as_view(),    name='patient_list'),
    path('patients/add/',                 views.PatientCreate.as_view(),  name='patient_add'),
    path('patients/<int:pk>/',            views.PatientDetail.as_view(),  name='patient_detail'),
    path('patients/<int:pk>/edit/',       views.PatientUpdate.as_view(),  name='patient_edit'),
    path('patients/<int:pk>/delete/',     views.PatientDelete.as_view(),  name='patient_delete'),

    # Médecins
    path('medecins/',                     views.MedecinList.as_view(),    name='medecin_list'),
    path('medecins/add/',                 views.MedecinCreate.as_view(),  name='medecin_add'),
    path('medecins/<int:pk>/',            views.MedecinDetail.as_view(),  name='medecin_detail'),
    path('medecins/<int:pk>/edit/',       views.MedecinUpdate.as_view(),  name='medecin_edit'),
    path('medecins/<int:pk>/delete/',     views.MedecinDelete.as_view(),  name='medecin_delete'),

    # Rendez-vous
    path('rendezvous/',                   views.RendezVousList.as_view(),    name='rdv_list'),
    path('rendezvous/add/',               views.RendezVousCreate.as_view(),  name='rdv_add'),
    path('rendezvous/<int:pk>/',          views.RendezVousDetail.as_view(),  name='rdv_detail'),
    path('rendezvous/<int:pk>/edit/',     views.RendezVousUpdate.as_view(),  name='rdv_edit'),
    path('rendezvous/<int:pk>/delete/',   views.RendezVousDelete.as_view(),  name='rdv_delete'),

    # Consultations
    path('consultations/',                views.ConsultationList.as_view(),    name='consultation_list'),
    path('consultations/add/',            views.ConsultationCreate.as_view(),  name='consultation_add'),
    path('consultations/<int:pk>/',       views.ConsultationDetail.as_view(),  name='consultation_detail'),
    path('consultations/<int:pk>/edit/',  views.ConsultationUpdate.as_view(),  name='consultation_edit'),
    path('consultations/<int:pk>/delete/',views.ConsultationDelete.as_view(),  name='consultation_delete'),

    # Dossiers médicaux
    path('dossiers/',                     views.DossierMedicalList.as_view(),    name='dossier_list'),
    path('dossiers/add/',                 views.DossierMedicalCreate.as_view(),  name='dossier_add'),
    path('dossiers/<int:pk>/',            views.DossierMedicalDetail.as_view(),  name='dossier_detail'),
    path('dossiers/<int:pk>/edit/',       views.DossierMedicalUpdate.as_view(),  name='dossier_edit'),
    path('dossiers/<int:pk>/delete/',     views.DossierMedicalDelete.as_view(),  name='dossier_delete'),

    # Factures
    path('factures/',                    views.FactureList.as_view(),    name='facture_list'),
    path('factures/add/',                views.FactureCreate.as_view(),  name='facture_add'),
    path('factures/<int:pk>/',           views.FactureDetail.as_view(),  name='facture_detail'),
    path('factures/<int:pk>/edit/',      views.FactureUpdate.as_view(),  name='facture_edit'),
    path('factures/<int:pk>/delete/',    views.FactureDelete.as_view(),  name='facture_delete'),
]