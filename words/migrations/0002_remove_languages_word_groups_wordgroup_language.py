# Generated by Django 4.0.3 on 2022-04-09 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languages',
            name='word_groups',
        ),
        migrations.AddField(
            model_name='wordgroup',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='words.languages'),
        ),
    ]
