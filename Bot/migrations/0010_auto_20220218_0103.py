# Generated by Django 3.2.9 on 2022-02-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0009_auto_20220218_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='elon',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='elon',
            name='elon_id',
            field=models.IntegerField(default=0),
        ),
    ]