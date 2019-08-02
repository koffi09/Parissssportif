# Generated by Django 2.2.3 on 2019-07-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myappparisportif', '0002_auto_20190729_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='parieurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('montant_parier', models.PositiveIntegerField()),
                ('choix_pays', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pays', models.CharField(max_length=255)),
                ('cote_pays', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_championat', models.CharField(max_length=255)),
                ('rencontre_pays', models.CharField(max_length=255)),
                ('date_rencontre', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Parisportif',
        ),
    ]