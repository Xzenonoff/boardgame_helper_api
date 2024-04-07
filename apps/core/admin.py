from django.contrib import admin

from apps.core.models import Category, Game, Session, Rule


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'player_quantity',
        'category'
    ]
    list_filter = ['name', 'player_quantity', 'category']
    search_fields = ['name', 'category']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        'game',
        'user'
    ]
    list_filter = ['game', 'user']
    search_fields = ['game']


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'game',
    ]
    list_filter = ['name']
    search_fields = ['name']
