from django.contrib import admin
from .models import User_Data,Scores


class FormAdmin(admin.ModelAdmin):
    list_display = ("first","last_name")

admin.site.register(User_Data,FormAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ("first","email","currentlevel","score")

admin.site.register(Scores,ScoreAdmin)
