# app_spp/forms.py

from django import forms
from .models import Siswa, Petugas, Kelas, Spp

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        fields = '__all__'

class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'

class SppForm(forms.ModelForm):
    class Meta:
        model = Spp
        fields = '__all__'
