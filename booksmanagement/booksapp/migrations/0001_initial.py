# Generated by Django 3.2 on 2024-01-30 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('read', models.CharField(choices=[('unread', '未読'), ('read', '既読')], default='unread', max_length=50)),
                ('p_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
