from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal
from datetime import datetime

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class Lapangan(models.Model):
    nama_lapangan = models.CharField(max_length=100)
    harga_per_jam = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_lapangan

class Reservasi(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.pelanggan.nama} - {self.lapangan.nama_lapangan} ({self.tanggal})"

    def clean(self):
        """Validasi agar jam_selesai > jam_mulai"""
        if self.jam_selesai <= self.jam_mulai:
            raise ValidationError("Jam selesai harus lebih besar dari jam mulai")

    def save(self, *args, **kwargs):
        # Jalankan validasi
        self.full_clean()

        # Gabungkan tanggal + jam
        start = datetime.combine(self.tanggal, self.jam_mulai)
        end = datetime.combine(self.tanggal, self.jam_selesai)

        # Hitung durasi dalam jam
        durasi = (end - start).total_seconds() / 3600

        if durasi <= 0:
            raise ValidationError("Durasi harus lebih dari 0 jam")

        # Konversi ke Decimal sebelum dikali
        durasi_decimal = Decimal(str(durasi))

        # Hitung total_harga otomatis
        self.total_harga = self.lapangan.harga_per_jam * durasi_decimal

        super().save(*args, **kwargs)
