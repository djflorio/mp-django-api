from rest_framework import serializers
from diner.models import MbBpm


class MbBpmSerializer(serializers.Serializer):
    recid = serializers.IntegerField(read_only=True)
    value = serializers.CharField(max_length=62)
    parent_id = serializers.IntegerField()

    def create(self, validated_data):
        return MbBpm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.value = validated_data('value', instance.value)
        instance.parent_id = validated_data('parent_id', instance.parent_id)
        instance.save()
        return instance