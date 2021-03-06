# Generated by Django 3.2.7 on 2021-09-21 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_test_link'),
        ('accounts', '0002_profile_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='questions.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
