# Generated by Django 4.2.6 on 2023-11-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_remove_message_receiver_remove_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='room',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
