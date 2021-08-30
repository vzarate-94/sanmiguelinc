# Generated by Django 3.2.4 on 2021-08-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_rooftop_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooftop',
            name='price',
            field=models.IntegerField(choices=[(1, 'Very Affordable'), (2, 'Affordable'), (3, 'Average'), (4, 'Expensive'), (5, 'Very Expensive')], default=1),
        ),
    ]