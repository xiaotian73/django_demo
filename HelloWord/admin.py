from django.contrib import admin
from HelloWord import models

class userAdmin(admin.ModelAdmin):
    fields = ('name','password')

admin.site.register(models.User,userAdmin)