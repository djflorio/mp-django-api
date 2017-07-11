from rest_framework import serializers
from diner.models import MbBpm, Metadata


class MbBpmSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbBpm
        fields = ('recid', 'value', 'parent_id')

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'