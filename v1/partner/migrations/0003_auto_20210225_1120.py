# Generated by Django 3.1.7 on 2021-02-25 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partner_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Pending'), (2, 'Waiting-Response'), (3, 'Triaged'), (4, 'Completed'), (5, 'Cancelled'), (6, 'Rejected')], default=0),
        ),
    ]
