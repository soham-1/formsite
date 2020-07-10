from django.shortcuts import render
from django.http import JsonResponse
from .models import details
import datetime
# Create your views here.

def index(request):
    if request.method == "POST" and request.is_ajax():
        try:
            print(request.POST)
            obj = details()
            obj.location = request.POST['location']
            obj.incidentDesc = request.POST['desc']
            obj.incidentTime = datetime.time(hour=int(request.POST['time'][:2]), minute=int(request.POST['time'][3:]))
            obj.incidentdate = datetime.date(int(request.POST['date'].split('-')[0]), int(request.POST['date'].split('-')[1]), int(request.POST['date'].split('-')[2]))
            obj.inciloc = request.POST['incLoc']
            obj.severity = request.POST['severity']
            obj.cause = request.POST['cause']
            obj.actionTaken = request.POST['action']
            obj.types = request.POST['type']
            obj.reporter = request.POST['reporter']
            obj.save()
            return JsonResponse({"error": "noerr"})
        except Exception as e:
            return JsonResponse({"error": e})
    return render(request, 'formapp/trail.html')