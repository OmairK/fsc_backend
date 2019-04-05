from rest_framework import serializers
from tournaments.models import TournamentFSC,TournamentITF,PlayerRankingsMS

class TournamentITFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentITF
        fields = ('name','venue','start_date','end_date','surface','grade','link','website')

class PlayerRankingsSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMS
        fields =('name','rank','movement','dob','events','points','ageGroup','category')

class TournamentFSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentFSC
        fields = ('name','age_group','venue','date','description','coordinator_contact','coordinator_name','coordinator_email')

        
