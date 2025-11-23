# reservasi/urls.py
from django.urls import path
from .views import (
    PelangganListView, PelangganDetailView, PelangganCreateView, PelangganUpdateView, PelangganDeleteView,
    ReservasiListView, ReservasiCreateView, ReservasiUpdateView, ReservasiDeleteView,
    LapanganListView, LapanganDetailView, LapanganCreateView, LapanganUpdateView, LapanganDeleteView
)

urlpatterns = [
    # ----------------------------
    # Pelanggan
    # ----------------------------
    path('', PelangganListView.as_view(), name='pelanggan-list'),
    path('tambah/', PelangganCreateView.as_view(), name='pelanggan-tambah'),
    path('<int:pk>/', PelangganDetailView.as_view(), name='pelanggan-detail'),
    path('<int:pk>/edit/', PelangganUpdateView.as_view(), name='pelanggan-edit'),
    path('<int:pk>/hapus/', PelangganDeleteView.as_view(), name='pelanggan-hapus'),

    # ----------------------------
    # Reservasi
    # ----------------------------
    path('reservasi/', ReservasiListView.as_view(), name='reservasi-list'),
    path('reservasi/tambah/', ReservasiCreateView.as_view(), name='reservasi-tambah'),
    path('reservasi/<int:pk>/edit/', ReservasiUpdateView.as_view(), name='reservasi-edit'),
    path('reservasi/<int:pk>/hapus/', ReservasiDeleteView.as_view(), name='reservasi-hapus'),

    # ----------------------------
    # Lapangan
    # ----------------------------
    path('lapangan/', LapanganListView.as_view(), name='lapangan-list'),
    path('lapangan/tambah/', LapanganCreateView.as_view(), name='lapangan-tambah'),
    path('lapangan/<int:pk>/', LapanganDetailView.as_view(), name='lapangan-detail'),
    path('lapangan/<int:pk>/edit/', LapanganUpdateView.as_view(), name='lapangan-edit'),
    path('lapangan/<int:pk>/hapus/', LapanganDeleteView.as_view(), name='lapangan-hapus'),
]
