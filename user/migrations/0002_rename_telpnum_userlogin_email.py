# Generated by Django 3.2.17 on 2023-09-09 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='telpnum',
            new_name='email',
        ),
    ]
