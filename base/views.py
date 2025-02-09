from django.shortcuts import render
from . models import *
from datetime import datetime, timedelta
hari_ini = datetime.now()
senin = hari_ini - timedelta(days=hari_ini.weekday())
sabtu = senin + timedelta(days=5)
tahun_sekarang = hari_ini.year
senin_formatted = senin.strftime('%Y-%m-%d')
sabtu_formatted = sabtu.strftime('%Y-%m-%d')

def index(request):
    set_kelas = JadwalMain.objects.values_list('Kelas', flat=True).distinct()
    semesters = JadwalMain.objects.values_list('Semester', flat=True).distinct()
    tahun_pelajaran = JadwalMain.objects.values_list('TahunPelajaran', flat=True).distinct()

    if request.method == 'POST':
        kelas = request.POST.get('kelas')
        semester = request.POST.get('semester')
        tahun_ajaran = request.POST.get('tahun_ajaran')

        jadwal_main_entry = JadwalMain.objects.filter(Kelas=kelas).first()
        if jadwal_main_entry:
            kelas_dipilih = jadwal_main_entry.Kelas
            jurusan = jadwal_main_entry.Jurusan
        else:
            kelas_dipilih = None
            jurusan = None

        jadwal_entries = Jadwal.objects.filter(Kelas__Kelas=kelas,
                                                     Kelas__Semester=semester,
                                                     Kelas__TahunPelajaran=tahun_ajaran)

        days = set(entry.Hari for entry in jadwal_entries)

        jadwal_data = {day: [] for day in days}

        for entry in jadwal_entries:
            jadwal_data[entry.Hari].append(entry)       

        context = {
            'set_kelas': set_kelas,
            'semesters': semesters,
            'tahun_pelajaran': tahun_pelajaran,
            'jadwal_data': jadwal_data,
            'kelas_dipilih': kelas_dipilih,
            'jurusan': jurusan,
            'senin': senin_formatted,
            'sabtu': sabtu_formatted,
            'tahun_sekarang': tahun_sekarang,
        }
        return render(request, 'index.html', context)

    context = {
        'set_kelas': set_kelas,
        'semesters': semesters,
        'tahun_pelajaran': tahun_pelajaran,
        'kelas_dipilih': None,
        'jurusan': None,
        'senin': senin_formatted,
        'sabtu': sabtu_formatted,
        'tahun_sekarang': tahun_sekarang,
    }

    return render(request, 'index.html', context)