# Generated by Django 4.0.1 on 2022-02-04 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gf', '0002_following_purged_alter_user_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeder',
            name='time_seeded',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='key',
            field=models.CharField(help_text='The setting key.', max_length=64, unique=True, verbose_name='Key'),
        ),
    ]
