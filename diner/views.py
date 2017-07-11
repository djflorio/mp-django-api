from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from diner.models import MbBpm
from diner.serializers import MbBpmSerializer

@csrf_exempt
def mb_bpm_list(request):
    """
    List all MbBpm entries, or create a new one.
    """
    if request.method == 'GET':
        mb_bpms = MbBpm.objects.all()
        serializer = MbBpmSerializer(mb_bpms, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MbBpmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def mb_bpm_detail(request, pk):
    """
    Retrieve, update, or delete a MbBpm
    """
    try:
        mb_bpm = MbBpm.objects.get(recid=pk)
    except MbBpm.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MbBpmSerializer(mb_bpm)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MbBpmSerializer(mb_bpm, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mp_bpm.delete()
        return HttpResponse(status=204)