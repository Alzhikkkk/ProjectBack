# Generated by Django 4.0.1 on 2022-04-05 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('author', '0012_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileIfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=55, null=True)),
                ('last_name', models.CharField(blank=True, max_length=55, null=True)),
                ('img_pro', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=55, null=True)),
                ('city', models.CharField(blank=True, max_length=55, null=True)),
                ('address', models.CharField(blank=True, max_length=55, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
