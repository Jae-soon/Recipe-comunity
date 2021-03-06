# Generated by Django 3.1.3 on 2021-05-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='share_recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('menu', models.CharField(choices=[('korean', '한식'), ('chinese', '중식'), ('western', '양식'), ('japanese', '일식')], max_length=10)),
                ('material', models.TextField()),
                ('how_Make', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
