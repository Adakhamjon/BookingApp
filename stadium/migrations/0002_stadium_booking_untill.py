# Generated by Django 5.0.1 on 2024-02-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='booking_untill',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]