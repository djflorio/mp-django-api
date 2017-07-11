from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from diner.models import MbBpm, Metadata
from diner.serializers import MbBpmSerializer, MetadataSerializer

@api_view(['GET', 'POST'])
def mb_bpm_list(request, format=None):
    """
    List all MbBpm entries, or create a new one.
    """
    if request.method == 'GET':
        mb_bpms = MbBpm.objects.all()
        serializer = MbBpmSerializer(mb_bpms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MbBpmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mb_bpm_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a MbBpm
    """
    try:
        mb_bpm = MbBpm.objects.get(recid=pk)
    except MbBpm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MbBpmSerializer(mb_bpm)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MbBpmSerializer(mb_bpm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mp_bpm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def metadata_list(request, format=None):
    """
    List all Metadata entries, or create a new one.
    """
    if request.method == 'GET':
        metadata = Metadata.objects.all()
        serializer = MetadataSerializer(metadata, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MetadataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def metadata_detail(request, pk, format=None):
    """
    Retrieve, update, or delete Metadata
    """
    try:
        metadata = Metadata.objects.get(recid=pk)
    except Metadata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MetadataSerializer(metadata)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MetadataSerializer(metadata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        metadata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)