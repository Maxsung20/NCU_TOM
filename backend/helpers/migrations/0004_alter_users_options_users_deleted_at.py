# Generated by Django 4.2.6 on 2024-07-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0003_announcements_deleted_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='users',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
