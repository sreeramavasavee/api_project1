# Generated by Django 4.2.7 on 2023-11-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('esal', models.IntegerField()),
                ('ejob', models.CharField(max_length=100)),
            ],
        ),
    ]
