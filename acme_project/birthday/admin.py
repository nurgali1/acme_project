from django.contrib import admin
from .models import Birthday

@admin.register(Birthday) 
class BirthdayAdmin(admin.ModelAdmin):
    pass
user = User.objects.get(username='nurgali')