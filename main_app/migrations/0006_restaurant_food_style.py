# Generated by Django 2.2.5 on 2019-09-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='food_style',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
