from django.contrib import admin

from lessons.models import Lesson, Subject, AttendanceJournal
from users.models import User

'''
class LessonStudentInline(admin.TabularInline):
    model = Lesson

class LessonAttendanceInline(admin.TabularInline):
    model = Lesson

class AttendanceStudentInline(admin.TabularInline):
    model = User
'''

class SubjectLessonInline(admin.TabularInline):
    model = Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'date']
    #inlines = [LessonStudentInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [SubjectLessonInline]

@admin.register(AttendanceJournal)
class AttendanceJournalAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'lesson', 'student', 'attended']
    #inlines = [LessonAttendanceInline, AttendanceStudentInline ]

