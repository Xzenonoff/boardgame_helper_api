from django.contrib import admin

from apps.core.models import Category, File, Game, Rule, Session


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_at",
        "updated_at",
    ]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "player_quantity",
        "category",
        "created_at",
        "updated_at",
    ]
    list_filter = ["name", "player_quantity", "category"]
    search_fields = ["name", "category"]


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "game",
        "user",
        "created_at",
        "updated_at",
    ]
    list_filter = ["game", "user"]
    search_fields = ["game"]


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "game",
        "file",
        "created_at",
        "updated_at",
    ]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "file",
        "created_at",
        "updated_at",
    ]
    list_filter = ["name"]
    search_fields = ["name"]
