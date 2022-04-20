# Generated by Django 4.0.3 on 2022-04-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_account_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_learner',
        ),
        migrations.AddField(
            model_name='account',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]