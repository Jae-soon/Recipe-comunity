# Generated by Django 3.1.3 on 2021-05-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_recipe', '0005_auto_20210511_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_recipe',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
