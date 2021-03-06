from rest_framework import serializers 

from tracking.models import Tracking


class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = "__all__"