# Generated by Django 4.0.3 on 2022-03-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_hr', models.IntegerField()),
                ('upload_mn', models.IntegerField()),
            ],
            options={
                'db_table': 'upload_time',
            },
        ),
    ]
