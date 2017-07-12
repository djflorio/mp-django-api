from diner.models import MbBpm, Metadata
from diner.serializers import MbBpmSerializer, MetadataSerializer
from rest_framework import generics


class MbBpmList(generics.ListCreateAPIView):
    queryset = MbBpm.objects.all()
    serializer_class = MbBpmSerializer

class MbBpmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MbBpm.objects.all()
    serializer_class = MbBpmSerializer

class MetadataList(generics.ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class MetadataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer