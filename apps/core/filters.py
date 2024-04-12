from django_filters import rest_framework as filters

from apps.core.models import Game, Rule, Session


class GameFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    player_quantity = filters.NumberFilter(lookup_expr="exact")

    class Meta:
        model = Game
        fields = ["category", "player_quantity"]


class SessionFilter(filters.FilterSet):
    game = filters.CharFilter(field_name="game__name", lookup_expr="icontains")

    class Meta:
        model = Session
        fields = ["game", "user"]


class RuleFilter(filters.FilterSet):
    game = filters.CharFilter(field_name="game__name", lookup_expr="icontains")

    class Meta:
        model = Rule
        fields = ["game"]
