# Generated by Django 4.2.6 on 2023-12-18 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0004_teachers_id_alter_teachers_cabinet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='cabinet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_app.cabinets'),
        ),
    ]
