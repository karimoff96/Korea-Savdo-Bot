# Generated by Django 3.2.6 on 2022-02-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0004_auto_20220203_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elon',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
