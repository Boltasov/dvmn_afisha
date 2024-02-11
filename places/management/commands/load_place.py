from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Event, Image


class Command(BaseCommand):
    help = 'Download a new place to data base'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            type=str,
            help='URL of json file with the palce data')

    def handle(self, *args, **kwargs):
        url = kwargs['json_url']
        response = requests.get(url)
        response.raise_for_status()
        raw_event = response.json()

        event, created = Event.objects.get_or_create(
            title=raw_event['title'],
            description_short=raw_event['description_short'],
            description_long=raw_event['description_long'],
            coordinates_lng=response.json()['coordinates']['lng'],
            coordinates_lat=response.json()['coordinates']['lat'],
        )

        if not created:
            print('Событие уже есть в базе')
            return

        img_urls = response.json()['imgs']
        for i, img_url in enumerate(img_urls):
            image_response = requests.get(img_url)
            response.raise_for_status()

            image_file = ContentFile(image_response.content)
            image = Image(
                order=i,
                event=event,
            )

            image.img.save(f'{event.title}_{i}', image_file, save=False)
            image.save()

        print('Событие добавлено в базу')
