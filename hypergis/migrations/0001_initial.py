# Generated by Django 3.1.7 on 2021-02-28 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('grass_age', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=20)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldGrass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FieldFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilot_name', models.CharField(max_length=50)),
                ('flight_time', models.TimeField(auto_now_add=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('drone_data', models.FileField(default='field_default_data.zip', upload_to='drone_data')),
                ('field_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hypergis.farmerfields')),
            ],
        ),
        migrations.AddField(
            model_name='farmerfields',
            name='grass_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hypergis.fieldgrass'),
        ),
        migrations.AddField(
            model_name='farmerfields',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
