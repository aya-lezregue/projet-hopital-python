from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    Patient, Medecin, Admin,
    RendezVous, Consultation, DossierMedical, Facture
)

class MedecinCreationForm(UserCreationForm):
    class Meta:
        model = Medecin
        fields = ("username", "email", "first_name", "last_name", "specialite")

class MedecinChangeForm(UserChangeForm):
    class Meta:
        model = Medecin
        fields = "__all__"

class MedecinAdmin(UserAdmin):
    add_form = MedecinCreationForm
    form = MedecinChangeForm
    model = Medecin

    list_display = ['username', 'email', 'first_name', 'last_name', 'specialite', 'is_active']
    
    # Customiser les champs affichés lors de l'édition
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'specialite')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Champs affichés lors de l'ajout d'un nouveau médecin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'specialite', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Patient)
admin.site.register(Medecin, MedecinAdmin)
admin.site.register(Admin)
admin.site.register(RendezVous)
admin.site.register(Consultation)
admin.site.register(DossierMedical)
admin.site.register(Facture)
