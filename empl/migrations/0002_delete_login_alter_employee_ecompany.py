# Generated by Django 4.0.5 on 2022-08-01 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empl', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='employee',
            name='eCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empl.company'),
        ),
    ]
