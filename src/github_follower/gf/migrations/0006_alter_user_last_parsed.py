# Generated by Django 4.0.1 on 2022-02-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gf', '0005_alter_target_user_options_remove_user_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_parsed',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
