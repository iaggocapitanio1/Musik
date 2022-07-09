from rest_framework import serializers

from . import models


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"
