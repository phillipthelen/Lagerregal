# Generated by Django 2.2.10 on 2020-03-12 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devicegroups', '0002_rm_read_perm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicegroup',
            options={'ordering': ['name'], 'verbose_name': 'Devicegroup', 'verbose_name_plural': 'Devicegroups'},
        ),
    ]