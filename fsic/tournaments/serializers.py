from rest_framework import serializers
from tournaments.models import TournamentFSC,TournamentITF,PlayerRankingsMS,PlayerRankingsMD,PlayerRankingsFS,PlayerRankingsFD

class TournamentITFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentITF
        fields = ('id','name','description','venue','start_date','end_date','surface','grade','link')

class PlayerRankingsSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMS
        fields =('id','name','ranking')

class PlayerRankingsSerializerMD(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMD
        fields =('id','name','ranking')
        
class PlayerRankingsSerializerFS(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsFS
        fields =('id','name','ranking')

class PlayerRankingsSerializerFD(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsFD
        fields =('id','name','ranking')

class TournamentFSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentFSC
        fields = ('id','name','age_group','venue','description')

        
