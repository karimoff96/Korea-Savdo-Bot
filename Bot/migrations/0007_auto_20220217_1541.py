# Generated by Django 3.2.9 on 2022-02-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0006_auto_20220216_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elon',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]