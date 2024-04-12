import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from nanoid import generate

User = get_user_model()

DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")


def generate_nanoid():
    return generate(
        "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", size=20
    )


class File(models.Model):
    id = models.CharField(
        max_length=20,
        primary_key=True,
        default=generate_nanoid,
        editable=False,
        unique=True,
    )
    name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.file}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    player_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(
        Game, on_delete=models.PROTECT, verbose_name="game", related_name="games"
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="user", related_name="users"
    )
    progress_info = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.game.name}:{self.id}"


class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    file = models.ForeignKey(File, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.game.name}"
