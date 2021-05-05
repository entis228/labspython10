# Generated by Django 2.2.12 on 2021-04-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('cont', models.FileField(upload_to='files/')),
                ('descr', models.TextField(blank=True)),
                ('downCount', models.IntegerField()),
            ],
        ),
    ]