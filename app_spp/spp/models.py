# app_spp/models.py

from django.db import models

class Kelas(models.Model):
    id_kelas = models.IntegerField(primary_key=True)
    nama_kelas = models.CharField(max_length=10)
    kompetensi_keahlian = models.CharField(max_length=50)

class Spp(models.Model):
    id_spp = models.IntegerField(primary_key=True)
    tahun = models.IntegerField()
    nominal = models.IntegerField()

class Petugas(models.Model):
    id_petugas = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    nama_petugas = models.CharField(max_length=35)
    level = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('petugas', 'Petugas')])

class Siswa(models.Model):
    nisn = models.CharField(max_length=10, primary_key=True)
    nis = models.CharField(max_length=8)
    nama = models.CharField(max_length=35)
    id_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=13)
    id_spp = models.ForeignKey(Spp, on_delete=models.CASCADE)

class Pembayaran(models.Model):
    id_pembayaran = models.IntegerField(primary_key=True)
    id_petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE)
    nisn = models.CharField(max_length=10)
    tgl_bayar = models.DateField()
    bulan_dibayar = models.CharField(max_length=8)
    tahun_dibayar = models.CharField(max_length=4)
    id_spp = models.ForeignKey(Spp, on_delete=models.CASCADE)
    jumlah_bayar = models.IntegerField()
