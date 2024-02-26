from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db import connection

from places.models import Event


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
                "detailsUrl": reverse(get_places, args=[event.pk])
            }
          }
        features.append(feature)

    context = {
        "places_geojson":
            {
                "type": "FeatureCollection",
                "features": features
            }
    }
    return render(request, 'index.html', context)


def get_places(request, id):
    event = get_object_or_404(Event.objects.prefetch_related('images'), pk=id)
    response = model_to_dict(event)
    response["imgs"] = [image.img.url for image in event.images.all()]
    return JsonResponse(
        response,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4
            }
        )
