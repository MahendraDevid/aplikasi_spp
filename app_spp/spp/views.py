# app_spp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Siswa, Petugas, Kelas, Spp
from .forms import SiswaForm, PetugasForm, KelasForm, SppForm

def siswa_list(request):
    siswa = Siswa.objects.all()
    return render(request, 'siswa_list.html', {'siswa': siswa})

def siswa_detail(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    return render(request, 'siswa_detail.html', {'siswa': siswa})

def siswa_new(request):
    if request.method == "POST":
        form = SiswaForm(request.POST)
        if form.is_valid():
            siswa = form.save(commit=False)
            siswa.save()
            return redirect('siswa_detail', nisn=siswa.nisn)
    else:
        form = SiswaForm()
    return render(request, 'siswa_edit.html', {'form': form})

def siswa_edit(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    if request.method == "POST":
        form = SiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            siswa = form.save(commit=False)
            siswa.save()
            return redirect('siswa_detail', nisn=siswa.nisn)
    else:
        form = SiswaForm(instance=siswa)
    return render(request, 'siswa_edit.html', {'form': form})

def siswa_delete(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    siswa.delete()
    return redirect('siswa_list')

def petugas_list(request):
    petugas = Petugas.objects.all()
    return render(request, 'petugas_list.html', {'petugas': petugas})

def petugas_detail(request, id_petugas):
    petugas = get_object_or_404(Petugas, id_petugas=id_petugas)
    return render(request, 'petugas_detail.html', {'petugas': petugas})

def petugas_new(request):
    if request.method == "POST":
        form = PetugasForm(request.POST)
        if form.is_valid():
            petugas = form.save(commit=False)
            petugas.save()
            return redirect('petugas_detail', id_petugas=petugas.id_petugas)
    else:
        form = PetugasForm()
    return render(request, 'petugas_edit.html', {'form': form})

def petugas_edit(request, id_petugas):
    petugas = get_object_or_404(Petugas, id_petugas=id_petugas)
    if request.method == "POST":
        form = PetugasForm(request.POST, instance=petugas)
        if form.is_valid():
            petugas = form.save(commit=False)
            petugas.save()
            return redirect('petugas_detail', id_petugas=petugas.id_petugas)
    else:
        form = PetugasForm(instance=petugas)
    return render(request, 'petugas_edit.html', {'form': form})

def petugas_delete(request, id_petugas):
    petugas = get_object_or_404(Petugas, id_petugas=id_petugas)
    petugas.delete()
    return redirect('petugas_list')

def kelas_list(request):
    kelas = Kelas.objects.all()
    return render(request, 'kelas_list.html', {'kelas': kelas})

def kelas_detail(request, id_kelas):
    kelas = get_object_or_404(Kelas, id_kelas=id_kelas)
    return render(request, 'kelas_detail.html', {'kelas': kelas})

def kelas_new(request):
    if request.method == "POST":
        form = KelasForm(request.POST)
        if form.is_valid():
            kelas = form.save(commit=False)
            kelas.save()
            return redirect('kelas_detail', id_kelas=kelas.id_kelas)
    else:
        form = KelasForm()
    return render(request, 'kelas_edit.html', {'form': form})

def kelas_edit(request, id_kelas):
    kelas = get_object_or_404(Kelas, id_kelas=id_kelas)
    if request.method == "POST":
        form = KelasForm(request.POST, instance=kelas)
        if form.is_valid():
            kelas = form.save(commit=False)
            kelas.save()
            return redirect('kelas_detail', id_kelas=kelas.id_kelas)
    else:
        form = KelasForm(instance=kelas)
    return render(request, 'kelas_edit.html', {'form': form})

def kelas_delete(request, id_kelas):
    kelas = get_object_or_404(Kelas, id_kelas=id_kelas)
    kelas.delete()
    return redirect('kelas_list')

def spp_list(request):
    spp = Spp.objects.all()
    return render(request, 'spp_list.html', {'spp': spp})

def spp_detail(request, id_spp):
    spp = get_object_or_404(Spp, id_spp=id_spp)
    return render(request, 'spp_detail.html', {'spp': spp})

def spp_new(request):
    if request.method == "POST":
        form = SppForm(request.POST)
        if form.is_valid():
            spp = form.save(commit=False)
            spp.save()
            return redirect('spp_detail', id_spp=spp.id_spp)
    else:
        form = SppForm()
    return render(request, 'spp_edit.html', {'form': form})

def spp_edit(request, id_spp):
    spp = get_object_or_404(Spp, id_spp=id_spp)
    if request.method == "POST":
        form = SppForm(request.POST, instance=spp)
        if form.is_valid():
            spp = form.save(commit=False)
            spp.save()
            return redirect('spp_detail', id_spp=spp.id_spp)
    else:
        form = SppForm(instance=spp)
    return render(request, 'spp_edit.html', {'form': form})

def spp_delete(request, id_spp):
    spp = get_object_or_404(Spp, id_spp=id_spp)
    spp.delete()
    return redirect('spp_list')