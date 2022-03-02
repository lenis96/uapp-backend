from django.contrib import admin
from .models import Semester,Asignature,AsignatureSemester


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['id','name']
# Register your models here.
admin.site.register(Semester, SemesterAdmin)

class AsignatureAdmin(admin.ModelAdmin):
    list_display =  ['id','name']

admin.site.register(Asignature,AsignatureAdmin)


class AsignatureSemesterAdmin(admin.ModelAdmin):
    list_display = ['id','asignature','semester','group']

admin.site.register(AsignatureSemester,AsignatureSemesterAdmin)