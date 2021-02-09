# Generated by Django 3.1.3 on 2021-02-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.CharField(max_length=250)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
