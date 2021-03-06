# Generated by Django 4.0.3 on 2022-03-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMatching',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_board_url', models.TextField()),
                ('from_club_id', models.CharField(max_length=20)),
                ('from_menu_id', models.CharField(max_length=20)),
                ('to_board_url', models.TextField()),
                ('to_club_id', models.CharField(max_length=20)),
                ('to_menu_id', models.CharField(max_length=20)),
                ('from_article_no', models.IntegerField()),
                ('to_article_no', models.IntegerField()),
                ('user_no', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'board_matching',
            },
        ),
    ]
