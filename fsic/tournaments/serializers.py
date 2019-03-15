from rest_framework import serializers
from tournaments.models import TournamentFSC,TournamentITF,PlayerRankingsMS,PlayerRankingsMD

class TournamentITFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentITF
        fields = ('id','name','venue','start_date','end_date','surface','grade','link','website')

class PlayerRankingsSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMS
        fields =('id','name','rank','movement','dob','events','points')

class PlayerRankingsSerializerMD(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMD
        fields =('id','name','rank','movement','dob','events','points')
        

class TournamentFSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentFSC
        fields = ('id','name','age_group','venue','date','description')

        
