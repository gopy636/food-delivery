# Generated by Django 3.2.4 on 2021-07-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='forgot_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='forgot_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
