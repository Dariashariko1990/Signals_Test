# Generated by Django 3.2.8 on 2021-10-14 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.subject')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='AttendanceJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField()),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson_attendance', to='lessons.lesson')),
            ],
            options={
                'verbose_name': 'Посещаемость',
            },
        ),
    ]
