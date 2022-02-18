# Generated by Django 3.2.6 on 2022-02-01 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, unique=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('lang', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elon_id', models.IntegerField(default=0, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.IntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, default=0, null=True)),
                ('journey', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('policy', models.CharField(blank=True, max_length=20, null=True)),
                ('korobka', models.CharField(blank=True, max_length=20, null=True)),
                ('fuel', models.CharField(blank=True, max_length=30, null=True)),
                ('comment', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('image', models.ImageField(upload_to='media')),
                ('memory', models.IntegerField(blank=True, default=0, null=True)),
                ('CPU', models.IntegerField(blank=True, default=0, null=True)),
                ('camera', models.CharField(blank=True, max_length=20, null=True)),
                ('zaryad', models.CharField(blank=True, max_length=20, null=True)),
                ('condition', models.CharField(blank=True, max_length=30, null=True)),
                ('display', models.CharField(blank=True, max_length=20, null=True)),
                ('processor', models.CharField(blank=True, max_length=30, null=True)),
                ('step', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bot.user')),
            ],
        ),
    ]
