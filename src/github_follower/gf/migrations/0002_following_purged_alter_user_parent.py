# Generated by Django 4.0.1 on 2022-02-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='purged',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
    ]
