from rest_framework import serializers
from tournaments.models import TournamentFSC,TournamentITF,PlayerRankingsMS

class TournamentITFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentITF
        fields = ('tournament_name','venue','start_date','end_date','surface','grade','link','website')

class PlayerRankingsSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = PlayerRankingsMS
        fields =('name','rank','movement','dob','events','points','age_group','category')

class TournamentFSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentFSC
        fields = ('tournament_name','age_group','tournament_venue','date','tournament_description','coordinator_name','coordinator_contact_number','coordinator_email','event_location_url')

        
