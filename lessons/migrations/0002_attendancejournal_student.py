# Generated by Django 3.2.8 on 2021-10-14 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancejournal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_attendance', to=settings.AUTH_USER_MODEL),
        ),
    ]
