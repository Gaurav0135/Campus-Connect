# Generated by Django 4.2.16 on 2024-12-22 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_notice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='caption',
            new_name='Ncaption',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='created_at',
            new_name='Ncreated_at',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='image',
            new_name='Nimage',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='user',
            new_name='Nuser',
        ),
    ]
