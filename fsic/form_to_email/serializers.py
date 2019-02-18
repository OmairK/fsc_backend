from rest_framework import serializers
from form_to_email.models import EmailBody

class EmailBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailBody
        fields = ('id','body')

