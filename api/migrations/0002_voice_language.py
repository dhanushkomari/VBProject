# Generated by Django 3.1.4 on 2021-10-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voice',
            name='language',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]