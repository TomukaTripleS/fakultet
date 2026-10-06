from django.contrib import admin

from .models import Department, Discipline, FacultyInfo, Program, Teacher

admin.site.register(Department)
admin.site.register(Discipline)
admin.site.register(FacultyInfo)
admin.site.register(Program)
admin.site.register(Teacher)
