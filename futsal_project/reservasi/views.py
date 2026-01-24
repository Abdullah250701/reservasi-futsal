from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Pelanggan, Reservasi, Lapangan
from .serializers import (
    PelangganSerializer,
    ReservasiSerializer,
    LapanganSerializer
)
from .permissions import IsStaffOrReadOnly
from .forms import PelangganForm, ReservasiForm


# =====================================================
# API VIEWS (DRF) - FINAL UAS
# =====================================================

# -----------------------------
# API PELANGGAN
# -----------------------------
class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all().order_by('-id')
    serializer_class = PelangganSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama', 'no_hp']
    ordering_fields = ['nama', 'no_hp']


# -----------------------------
# API RESERVASI
# -----------------------------
class ReservasiViewSet(viewsets.ModelViewSet):
    queryset = Reservasi.objects.all().order_by('-tanggal')
    serializer_class = ReservasiSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'pelanggan__nama',
        'lapangan__nama_lapangan'
    ]
    ordering_fields = ['tanggal']


# -----------------------------
# API LAPANGAN
# -----------------------------
class LapanganViewSet(viewsets.ModelViewSet):
    queryset = Lapangan.objects.all().order_by('nama_lapangan')
    serializer_class = LapanganSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lapangan']
    ordering_fields = ['nama_lapangan', 'harga_per_jam']


# =====================================================
# WEB VIEWS (CBV)
# =====================================================

# -----------------------------
# PELANGGAN
# -----------------------------
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


# -----------------------------
# RESERVASI
# -----------------------------
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


# -----------------------------
# LAPANGAN
# -----------------------------
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
