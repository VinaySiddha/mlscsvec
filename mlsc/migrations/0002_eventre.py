# Generated by Django 4.2 on 2024-03-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('rollnumber', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('event', models.CharField(max_length=50)),
            ],
        ),
    ]
