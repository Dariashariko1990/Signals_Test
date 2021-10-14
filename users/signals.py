from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from lessons.models import AttendanceJournal


@receiver(user_logged_in)
def login_handler(sender, user, request, **kwargs):
    lessons_unattended = AttendanceJournal.objects.all().filter(student=user.id).filter(attended=False).count()
    if lessons_unattended >= 2:
        print(f"Предупреждение: Вы пропустили {lessons_unattended} урока.")