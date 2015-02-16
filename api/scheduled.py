from django.shortcuts import render
from django.http import HttpResponse

from bvggrabber.api.scheduleddeparture import ScheduledDepartureQueryApi, Vehicle

def show(request):
  vehicles = vehicles_to_bits(request.GET.get('vehicles', 'U').split(','))
  station = request.GET.get('station', '')

  try:
    limit = int(request.GET.get('limit', 9))
  except ValueError:
    limit = 9

  resp = ScheduledDepartureQueryApi(station, vehicles=vehicles, limit=limit).call()

  return HttpResponse(resp.json, content_type='application/json')

def vehicles_to_bits(vehicles):
  vehicle_bits = 0

  for vehicle in vehicles:
    vehicle = vehicle.upper()

    if vehicle == 'S':
        vehicle_bits |= Vehicle.S
    elif vehicle == 'U':
        vehicle_bits |= Vehicle.U
    elif vehicle == 'TRAM':
        vehicle_bits |= Vehicle.TRAM
    elif vehicle == 'BUS':
        vehicle_bits |= Vehicle.BUS
    elif vehicle == 'FERRY':
        vehicle_bits |= Vehicle.FERRY
    elif vehicle == 'RB':
        vehicle_bits |= Vehicle.RB
    elif vehicle == 'IC':
        vehicle_bits |= Vehicle.IC

  return vehicle_bits
