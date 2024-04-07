from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    player_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Session(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT, verbose_name='game', related_name='games')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user', related_name='users')
    progress_info = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
