from django import forms
from .models import Pelanggan, Reservasi

class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = ['nama', 'no_hp']

# ===========================
# Form untuk membuat Reservasi baru
# ===========================
class ReservasiForm(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['pelanggan', 'lapangan', 'tanggal', 'jam_mulai', 'jam_selesai', 'total_harga']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
            'jam_mulai': forms.TimeInput(attrs={'type': 'time'}),
            'jam_selesai': forms.TimeInput(attrs={'type': 'time'}),
        }
