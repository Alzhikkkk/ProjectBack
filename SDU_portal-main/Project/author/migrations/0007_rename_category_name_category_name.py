# Generated by Django 4.0.1 on 2022-03-12 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_category_blogs_category_alter_blogs_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
