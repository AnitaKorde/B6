# Generated by Django 4.0.1 on 2022-01-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.CharField(default='y', max_length=1),
        ),
    ]
