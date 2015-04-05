from django.shortcuts import render
from django.http import HttpResponse

from bvggrabber.api.actualdeparture import ActualDepartureQueryApi

def show(request):
  station = request.GET.get('station', '')

  try:
    limit = int(request.GET.get('limit', 9))
  except ValueError:
    limit = 9

  # more recent versions take limit
  # waiting for update
  resp = ActualDepartureQueryApi(station).call()

  return HttpResponse(resp.json, content_type='application/json')
