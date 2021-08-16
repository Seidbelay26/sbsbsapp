from django.contrib import admin

# Register your models here.
from .models import Meetme, Location ,Participants

class MeetmeAdmin(admin.ModelAdmin):
    list_display = ("title","date","location")
    list_filter = ('location',"date")
    prepopulated_fields = {'slug':('title', )}

'''class Recordparticipants(admin.ModelAdmin):
    list_display = ("name","email")'''
    

admin.site.register(Meetme, MeetmeAdmin)
admin.site.register(Location)
admin.site.register(Participants)#, Recordparticipants)