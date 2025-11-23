# reservasi/serializers.py
from rest_framework import serializers
from .models import Pelanggan, Reservasi, Lapangan

# --- Serializers Pelanggan ---
class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ['id', 'nama', 'no_hp']

# --- Serializers Lapangan ---
class LapanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lapangan
        fields = ['id', 'nama_lapangan', 'harga_per_jam']

# --- Serializers Reservasi ---
class ReservasiSerializer(serializers.ModelSerializer):
    # Untuk POST/PUT gunakan PrimaryKeyRelatedField
    pelanggan = serializers.PrimaryKeyRelatedField(queryset=Pelanggan.objects.all())
    lapangan = serializers.PrimaryKeyRelatedField(queryset=Lapangan.objects.all())

    # Optional: tampilkan nested detail saat GET
    pelanggan_detail = PelangganSerializer(source='pelanggan', read_only=True)
    lapangan_detail = LapanganSerializer(source='lapangan', read_only=True)

    class Meta:
        model = Reservasi
        fields = ['id','pelanggan','lapangan','tanggal','jam_mulai','jam_selesai','total_harga','pelanggan_detail','lapangan_detail'
        ]
