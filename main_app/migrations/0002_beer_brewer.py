# Generated by Django 2.2.5 on 2019-09-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='brewer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
