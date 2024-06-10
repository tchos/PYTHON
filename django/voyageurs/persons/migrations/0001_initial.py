# Generated by Django 4.2 on 2024-06-10 12:56

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
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('date_naissance', models.DateField()),
                ('numero_cni', models.CharField(max_length=32)),
                ('numero_passeport', models.CharField(blank=True, max_length=32, null=True)),
                ('mouvement', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ENTREE'), (2, 'SORTIE')], null=True)),
                ('date_mouvement', models.DateField()),
                ('provenance_destination', models.CharField(max_length=64)),
                ('frontiere', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'AEROPORT DE NSIMALEN'), (2, 'AEROPORT DE DOUALA'), (3, 'AEROPORT DE GAROUA ET BANKI'), (4, 'FRONTIERE DE ELOK'), (5, 'FRONTIERE DE IDENAU'), (6, 'FRONTIERE DE ABANG MINKO'), (7, 'FRONTIERE DE KYE OSSI'), (8, 'DONNEES CNPS')], null=True)),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('collector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
