from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from models.game import Game


class GameView(ViewSet):

    def list(self, request):
        """Handle GET for all games
        """
        games = Game.objects.all()

        # TODO: Support filtering by game type

        serializer = GameSerializer(
            games, many=True, context={'request': request}
        )
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'number_of_players', 'est_time', 'age_rec', 'player')
        depth = 1