from django.contrib import admin

# Register your models here.
from .models import List, Game_list, Game, Game_type, Parkinson_phase, Patient

admin.site.register(List)
admin.site.register(Game_list)
admin.site.register(Game)
admin.site.register(Game_type)
