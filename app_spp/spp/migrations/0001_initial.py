# Generated by Django 4.2 on 2023-11-13 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id_kelas', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=10)),
                ('kompetensi_keahlian', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Petugas',
            fields=[
                ('id_petugas', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=32)),
                ('nama_petugas', models.CharField(max_length=35)),
                ('level', models.CharField(choices=[('admin', 'Admin'), ('petugas', 'Petugas')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Spp',
            fields=[
                ('id_spp', models.IntegerField(primary_key=True, serialize=False)),
                ('tahun', models.IntegerField()),
                ('nominal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('nisn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nis', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=35)),
                ('alamat', models.TextField()),
                ('no_telp', models.CharField(max_length=13)),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.kelas')),
                ('id_spp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.spp')),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id_pembayaran', models.IntegerField(primary_key=True, serialize=False)),
                ('nisn', models.CharField(max_length=10)),
                ('tgl_bayar', models.DateField()),
                ('bulan_dibayar', models.CharField(max_length=8)),
                ('tahun_dibayar', models.CharField(max_length=4)),
                ('jumlah_bayar', models.IntegerField()),
                ('id_petugas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.petugas')),
                ('id_spp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.spp')),
            ],
        ),
    ]
