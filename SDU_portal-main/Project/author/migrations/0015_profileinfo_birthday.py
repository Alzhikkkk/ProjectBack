# Generated by Django 4.0.1 on 2022-04-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0014_rename_profileifo_profileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]