import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

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
            defaults={
                'short_description': raw_event['short_description'],
                'long_description': raw_event['long_description'],
                'coordinates_lng': response.json()['coordinates']['lng'],
                'coordinates_lat': response.json()['coordinates']['lat'],
            },
        )

        if not created:
            print('Событие уже есть в базе')
            return

        img_urls = response.json()['imgs']
        for img_order, img_url in enumerate(img_urls):
            image_response = requests.get(img_url)
            response.raise_for_status()

            img_name = f'{event.title}_{img_order}'
            image_file = ContentFile(image_response.content, name=img_name)
            image = Image.objects.create(
                order=img_order,
                event=event,
            )

            image.img.save(image_file, save=True)

        print('Событие добавлено в базу')
