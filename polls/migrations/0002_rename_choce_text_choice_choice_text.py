# Generated by Django 4.1.5 on 2023-01-24 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choce_text',
            new_name='choice_text',
        ),
    ]
