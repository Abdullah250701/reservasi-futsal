# reservasi/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PelangganViewSet, ReservasiViewSet, LapanganViewSet

# Buat router dan daftarkan semua ViewSet
router = DefaultRouter()
router.register(r'pelanggan', PelangganViewSet, basename='pelanggan')
router.register(r'reservasi', ReservasiViewSet, basename='reservasi')
router.register(r'lapangan', LapanganViewSet, basename='lapangan')

# URL API ditentukan otomatis oleh router
urlpatterns = [
    path('', include(router.urls)),
]


# reservasi/api_urls.py
# from django.urls import path
# from .views import (
#     PelangganListAPIView, PelangganDetailAPIView,
#     ReservasiListAPIView, ReservasiDetailAPIView,
#     LapanganListAPIView, LapanganDetailAPIView
# )

# urlpatterns = [
    # API Pelanggan
    # path('pelanggan/', PelangganListAPIView.as_view(), name='api-pelanggan-list'),
    # path('pelanggan/<int:pk>/', PelangganDetailAPIView.as_view(), name='api-pelanggan-detail'),

    # API Reservasi
    # path('reservasi/', ReservasiListAPIView.as_view(), name='api-reservasi-list'),
    # path('reservasi/<int:pk>/', ReservasiDetailAPIView.as_view(), name='api-reservasi-detail'),

    # API Lapangan
    # path('lapangan/', LapanganListAPIView.as_view(), name='api-lapangan-list'),
    # path('lapangan/<int:pk>/', LapanganDetailAPIView.as_view(), name='api-lapangan-detail'),
# ]
