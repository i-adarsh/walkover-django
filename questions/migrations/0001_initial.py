# Generated by Django 3.2.7 on 2021-09-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(max_length=250)),
                ('option1', models.TextField(max_length=100)),
                ('option2', models.TextField(max_length=100)),
                ('option3', models.TextField(max_length=100)),
                ('option4', models.TextField(max_length=100)),
                ('correct', models.TextField(max_length=100)),
            ],
        ),
    ]
