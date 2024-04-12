from rest_framework import serializers

from apps.core.models import Category, File, Game, Rule, Session
from apps.users.serializers import UserSerializer


class FileListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ["id", "name", "slug", "file", "created_at", "updated_at"]


class FileCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        allow_empty_file=False, allow_null=False, write_only=True
    )

    class Meta:
        model = File
        fields = ["id", "name", "file", "created_at", "updated_at"]
        read_only_fields = ["id", "name", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class GameCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "description",
            "player_quantity",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class GameSerializer(GameCreateSerializer):
    category = CategorySerializer()


class SessionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ["id", "game", "user", "progress_info", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class SessionSerializer(SessionCreateSerializer):
    game = GameSerializer()
    user = UserSerializer()


class RuleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = [
            "id",
            "name",
            "description",
            "game",
            "file",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class RuleSerializer(RuleCreateSerializer):
    game = GameSerializer()
    file = FileListRetrieveSerializer()
