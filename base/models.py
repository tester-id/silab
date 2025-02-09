from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

# Create your models here.

PILIHAN_HARI = [
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
    ]

SESI = [
        ('Materi', 'Materi'),
        ('Praktek', 'Praktek'),
        ('Ujian', 'Ujian'),
        ('Diskusi', 'Diskusi'),
        ('Presentasi', 'Presentasi'),
    ]

class Jurusan(models.Model):
    NamaJurusan = models.CharField(max_length=100,primary_key=True)
    KepalaJurusan = models.CharField(max_length=100)
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Jurusan"
      verbose_name_plural = "Jurusan"
    def __str__(self):
        return self.NamaJurusan

class Guru(AbstractUser):
    NamaAwal = models.CharField(max_length=100,null=True)
    NamaTengah = models.CharField(max_length=100,null=True,blank=True)
    NamaAkhir = models.CharField(max_length=100,null=True,blank=True)
    Jurusan = models.ForeignKey(Jurusan,on_delete=models.CASCADE,null=True)
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Guru"
      verbose_name_plural = "Guru"
    def __str__(self):
        if self.NamaAwal or self.NamaTengah or self.NamaAkhir:
            return f"{self.NamaAwal or ''} {self.NamaTengah or ''} {self.NamaAkhir or ''}".strip()
        return self.username

class JadwalMain(models.Model):
    TahunPelajaran = models.CharField(max_length=9)
    Kelas = models.CharField(max_length=100,primary_key=True,editable=True)
    Semester  = models.CharField(max_length=100)
    Jurusan = models.ForeignKey(Jurusan,on_delete=models.CASCADE)
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Kelas

class NamaMapel(models.Model):
    Mapel = models.CharField(max_length=50)
    KodeMapel = models.CharField(max_length=10,primary_key=True)
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    DeskripsiMapel = models.CharField(max_length=200)
    def __str__(self):
        return self.Mapel
    class Meta:
        unique_together = (('Mapel', 'KodeMapel'),)

class Ruang(models.Model):
    Ruang = models.CharField(max_length=50,primary_key=True)
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Ruang

class Jadwal(models.Model):
    NamaMapel = models.ForeignKey(NamaMapel, on_delete=models.CASCADE)
    Guru = models.ForeignKey(Guru,on_delete=models.CASCADE)   
    Ruang = models.ForeignKey(Ruang,on_delete=models.CASCADE) 
    WaktuMulai = models.TimeField()
    WaktuSelesai = models.TimeField()
    Hari = models.CharField(max_length=100, choices=PILIHAN_HARI)
    Kelas = models.ForeignKey(JadwalMain,on_delete=models.CASCADE)   
    TerdaftarTanggal = models.DateTimeField(auto_now_add=True)
    TipeSesi = models.CharField(max_length=100, choices=SESI)