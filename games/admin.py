from django.contrib import admin
from .models import Developer, Genres, Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "release_date", "is_free")
    list_filter = ("is_free", "developer")
    search_fields = ("title",)

admin.site.register(Developer)
admin.site.register(Genres)
admin.site.register(Game, GameAdmin)
