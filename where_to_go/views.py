from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from places.models import Event
from django.forms.models import model_to_dict
from django.urls import reverse


def show_afisha(request):
    features = []
    events = Event.objects.all()
    for event in events:
        feature = {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [event.coordinates_lng, event.coordinates_lat]
            },
            "properties": {
              "title": event.title,
              "placeId": event.pk,
              "detailsUrl": reverse(places, args=[event.pk])
            }
          }
        features.append(feature)

    context = {"places_geojson":
      {
        "type": "FeatureCollection",
        "features": features
      }
    }
    return render(request, 'index.html', context)


def places1(request, id):
    event = Event.objects.get(pk=id)
    return HttpResponse(f"{event}")


def places(request, id):
    event = Event.objects.get(pk=id)
    response = model_to_dict(event)
    response["imgs"] = [image.img.url for image in event.images_set.all()]
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
