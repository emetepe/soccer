from django.contrib import admin

from .models import Team, Stadium

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'emblem_pic', 
        'coach_name', 
        'coach_pic', 
        'shirt_pic', 
        'stadium'
    )

class StadiumAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'pic'
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium, StadiumAdmin)
