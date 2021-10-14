from django.db import models

from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return '{}'.format(self.id)


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return '{}'.format(self.id)


class AttendanceJournal(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="lesson_attendance", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(User, related_name='student_attendance', on_delete=models.CASCADE)
    attended = models.BooleanField()

    class Meta:
        verbose_name = 'Посещаемость'

    def __str__(self):
        return '{}'.format(self.id)

