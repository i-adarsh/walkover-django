# Generated by Django 3.2.7 on 2021-09-21 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_test_link'),
        ('accounts', '0005_alter_takenquiz_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takenquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.test'),
        ),
    ]
