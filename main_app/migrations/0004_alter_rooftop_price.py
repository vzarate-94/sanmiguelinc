# Generated by Django 3.2.4 on 2021-08-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rooftop_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooftop',
            name='price',
            field=models.IntegerField(choices=[(1, 'Very Expensive'), (2, 'Expensive'), (3, 'Average'), (4, 'Afordable'), (5, 'Very Affordable')], default=1, max_length=1),
        ),
    ]
