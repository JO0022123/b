# Generated by Django 4.2.4 on 2023-08-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_emp1_delete_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=255)),
            ],
        ),
    ]