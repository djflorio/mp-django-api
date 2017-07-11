from rest_framework import serializers
from diner.models import MbBpm


class MbBpmSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbBpm
        fields = ('recid', 'value', 'parent_id')