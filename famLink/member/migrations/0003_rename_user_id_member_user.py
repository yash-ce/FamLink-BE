# Generated by Django 4.1.5 on 2023-01-28 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_rename_members_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='user_id',
            new_name='user',
        ),
    ]