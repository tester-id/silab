from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django import forms
from django.utils.html import format_html

# Register your models here.
class JurusanAdmin(admin.ModelAdmin):
    list_display = ('NamaJurusan', 'KepalaJurusan', 'registered_date_badge')
    list_filter = ('KepalaJurusan', 'TerdaftarTanggal')
    search_fields = ('NamaJurusan', 'KepalaJurusan')
    date_hierarchy = 'TerdaftarTanggal'
    list_editable=('KepalaJurusan',)
    list_per_page = 10   
    list_max_show_all = 10
    def registered_date_badge(self, obj):
        return format_html('<i class="fas fa-calendar-alt text-info"></i><span class="badge badge-dark p-2 ml-2 text-white">{}</span>', obj.TerdaftarTanggal.strftime('%Y-%m-%d'))
    registered_date_badge.short_description = 'Terdaftar Tanggal'
admin.site.register(Jurusan, JurusanAdmin)

class GuruAdmin(UserAdmin):
    list_display = ('username', 'NamaAwal','NamaAkhir',"NamaTengah", 'email', 'Jurusan', 'registered_date_badge')
    list_filter = ('Jurusan', 'TerdaftarTanggal')
    search_fields = ('username', 'email')
    list_per_page = 10   
    list_max_show_all = 10
    list_editable=('NamaAwal','NamaAkhir',"NamaTengah", 'email', 'Jurusan',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('email','NamaAwal','NamaAkhir',"NamaTengah")
        }),
        ('Department Info', {
            'fields': ('Jurusan',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    def registered_date_badge(self, obj):
        return format_html('<i class="fas fa-calendar-alt text-info"></i><span class="badge badge-dark p-2 ml-2 text-white">{}</span>', obj.TerdaftarTanggal.strftime('%Y-%m-%d'))
    registered_date_badge.short_description = 'Terdaftar Tanggal'
admin.site.register(Guru, GuruAdmin)

class JadwalMainAdmin(admin.ModelAdmin):
    list_display = ('TahunPelajaran', 'Kelas', 'Semester', 'Jurusan', 'registered_date_badge')
    list_filter = ('TahunPelajaran', 'Semester', 'Jurusan', 'TerdaftarTanggal')
    search_fields = ('TahunPelajaran', 'Kelas', 'Semester')
    date_hierarchy = 'TerdaftarTanggal'
    #list_editable=('Jurusan',)
    list_per_page = 10   
    list_max_show_all = 10
    list_editable=( 'Semester', 'Jurusan',)
    def registered_date_badge(self, obj):
        return format_html('<i class="fas fa-calendar-alt text-info"></i><span class="badge badge-dark p-2 ml-2 text-white">{}</span>', obj.TerdaftarTanggal.strftime('%Y-%m-%d'))
    registered_date_badge.short_description = 'Terdaftar Tanggal'
admin.site.register(JadwalMain, JadwalMainAdmin)

class TimePickerWidget(forms.TimeInput):
    template_name = 'widgets/time_picker.html'
    
class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'
        widgets = {
            'WaktuMulai': TimePickerWidget(),
            'WaktuSelesai': TimePickerWidget(),
        }

class JadwalAdmin(admin.ModelAdmin):
    form = JadwalForm
    list_display = ('id','Hari','NamaMapel', 'Ruang', 'WaktuMulai', 'WaktuSelesai',  'Kelas', 'registered_date_badge')
    list_filter = ('Hari', 'Kelas', 'TerdaftarTanggal')
    search_fields = ('NamaMapel', 'Ruang')
    date_hierarchy = 'TerdaftarTanggal'
    list_editable=('NamaMapel','Hari', 'Ruang', 'Kelas',)
    list_per_page = 5   
    list_max_show_all = 5
    def registered_date_badge(self, obj):
        return format_html('<i class="fas fa-calendar-alt text-info"></i><span class="badge badge-dark p-2 ml-2 text-white">{}</span>', obj.TerdaftarTanggal.strftime('%Y-%m-%d'))
    registered_date_badge.short_description = 'Terdaftar Tanggal'
admin.site.register(Jadwal, JadwalAdmin)

@admin.register(NamaMapel)
class NamaMapelAdmin(admin.ModelAdmin):
    list_display = ('KodeMapel','DeskripsiMapel','Mapel',  )
    search_fields = ('Mapel', 'KodeMapel', 'DeskripsiMapel')
    list_per_page = 10   
    list_max_show_all = 10
    list_editable=('Mapel','DeskripsiMapel',)


admin.site.register(Ruang)