# Generated by Django 3.2.9 on 2022-02-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0013_alter_elon_elon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elon',
            name='elon_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0, null=True, unique=True),
        ),
    ]