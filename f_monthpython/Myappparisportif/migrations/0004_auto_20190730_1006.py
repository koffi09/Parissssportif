# Generated by Django 2.2.3 on 2019-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myappparisportif', '0003_auto_20190729_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rencontre',
            name='date_rencontre',
            field=models.DateTimeField(verbose_name='Date_rencontre'),
        ),
    ]
