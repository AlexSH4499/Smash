from rest_framework import serializers
from tierlist.models import Tier
from tierlist.models import Fighter


class FighterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fighter
        fields = ('id', 'name', 'img')
