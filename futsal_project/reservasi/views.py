# reservasi/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Pelanggan, Reservasi, Lapangan
from .forms import PelangganForm

# ----------------------------
# API VIEWS DRF
# ----------------------------
# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from .serializers import PelangganSerializer, ReservasiSerializer, LapanganSerializer

# ----------------------------
# API VIEWS DRF - ModelViewSet
# ----------------------------
from rest_framework import viewsets
from .serializers import PelangganSerializer, ReservasiSerializer, LapanganSerializer
from .models import Pelanggan, Reservasi, Lapangan

# API Pelanggan
class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all().order_by('-id')
    serializer_class = PelangganSerializer

# API Reservasi
class ReservasiViewSet(viewsets.ModelViewSet):
    queryset = Reservasi.objects.all().order_by('-tanggal')
    serializer_class = ReservasiSerializer

# API Lapangan
class LapanganViewSet(viewsets.ModelViewSet):
    queryset = Lapangan.objects.all().order_by('nama_lapangan')
    serializer_class = LapanganSerializer


# ----------------------------
# API PELANGGAN
# ----------------------------
# class PelangganListAPIView(ListAPIView):
#     queryset = Pelanggan.objects.all()
#     serializer_class = PelangganSerializer

# class PelangganDetailAPIView(RetrieveAPIView):
#     queryset = Pelanggan.objects.all()
#     serializer_class = PelangganSerializer

# ----------------------------
# API RESERVASI
# ----------------------------
# class ReservasiListAPIView(ListAPIView):
#     queryset = Reservasi.objects.all()
#     serializer_class = ReservasiSerializer

# class ReservasiDetailAPIView(RetrieveAPIView):
#     queryset = Reservasi.objects.all()
#     serializer_class = ReservasiSerializer

# ----------------------------
# API LAPANGAN
# ----------------------------
# class LapanganListAPIView(ListAPIView):
#     queryset = Lapangan.objects.all()
#     serializer_class = LapanganSerializer

# class LapanganDetailAPIView(RetrieveAPIView):
#     queryset = Lapangan.objects.all()
#     serializer_class = LapanganSerializer

# ----------------------------
# PELANGGAN (WEB VIEWS)
# ----------------------------
class PelangganListView(ListView):
    model = Pelanggan

class PelangganDetailView(DetailView):
    model = Pelanggan

class PelangganCreateView(CreateView):
    model = Pelanggan
    form_class = PelangganForm
    template_name = 'reservasi/pelanggan_form.html'
    success_url = reverse_lazy('pelanggan-list')

class PelangganUpdateView(UpdateView):
    model = Pelanggan
    form_class = PelangganForm
    template_name = 'reservasi/pelanggan_form.html'
    success_url = reverse_lazy('pelanggan-list')

class PelangganDeleteView(DeleteView):
    model = Pelanggan
    template_name = 'reservasi/pelanggan_confirm_delete.html'
    success_url = reverse_lazy('pelanggan-list')

# ----------------------------
# RESERVASI (WEB VIEWS)
# ----------------------------
class ReservasiForm(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['pelanggan', 'lapangan', 'tanggal', 'jam_mulai', 'jam_selesai', 'total_harga']

class ReservasiListView(ListView):
    model = Reservasi

class ReservasiCreateView(CreateView):
    model = Reservasi
    form_class = ReservasiForm
    template_name = 'reservasi/reservasi_form.html'
    success_url = reverse_lazy('reservasi-list')

class ReservasiUpdateView(UpdateView):
    model = Reservasi
    form_class = ReservasiForm
    template_name = 'reservasi/reservasi_form.html'
    success_url = reverse_lazy('reservasi-list')

class ReservasiDeleteView(DeleteView):
    model = Reservasi
    template_name = 'reservasi/reservasi_confirm_delete.html'
    success_url = reverse_lazy('reservasi-list')

# ----------------------------
# LAPANGAN (WEB VIEWS)
# ----------------------------
class LapanganListView(ListView):
    model = Lapangan

class LapanganDetailView(DetailView):
    model = Lapangan

class LapanganCreateView(CreateView):
    model = Lapangan
    fields = ['nama_lapangan', 'harga_per_jam']
    template_name = 'reservasi/lapangan_form.html'
    success_url = reverse_lazy('lapangan-list')

class LapanganUpdateView(UpdateView):
    model = Lapangan
    fields = ['nama_lapangan', 'harga_per_jam']
    template_name = 'reservasi/lapangan_form.html'
    success_url = reverse_lazy('lapangan-list')

class LapanganDeleteView(DeleteView):
    model = Lapangan
    template_name = 'reservasi/lapangan_confirm_delete.html'
    success_url = reverse_lazy('lapangan-list')
