from rest_framework import serializers
from tournaments.models import TournamentFSC,TournamentITF,PlayerRankingsMS

class TournamentITFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentITF
        fields = ('id','name','description','venue','start_date','end_date','surface','grade','link')

class PlayerRankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMS
        fields =('id','name','ranking')

class TournamentFSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentFSC
        fields = ('id','name','age_group','venue','description')

        
