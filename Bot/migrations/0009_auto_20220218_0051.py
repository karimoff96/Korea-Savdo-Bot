# Generated by Django 3.2.9 on 2022-02-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0008_alter_elon_elon_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elon',
            name='id',
        ),
        migrations.AlterField(
            model_name='elon',
            name='elon_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]