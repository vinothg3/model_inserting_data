# Generated by Django 4.1.7 on 2023-04-03 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('Topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField()),
                ('Topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
