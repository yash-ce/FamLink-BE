# Generated by Django 4.1.5 on 2023-01-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_rename_user_id_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='relation',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
