# Generated by Django 4.1.5 on 2023-01-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
