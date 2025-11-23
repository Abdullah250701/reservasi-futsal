from django.contrib import admin
from .models import Pelanggan, Lapangan

admin.site.register(Pelanggan)
admin.site.register(Lapangan)  # Daftarkan model baru
