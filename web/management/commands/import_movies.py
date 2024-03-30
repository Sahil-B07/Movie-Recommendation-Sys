import csv
from django.core.management.base import BaseCommand
from web.models import Movie


class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:

                Movie.objects.create(
                    movie_id=row['id'],
                    title=row['original_title'],
                    genres=row['genres'],
                    overview=row['overview'],
                    popularity=row['popularity'],
                    vote_average=row['vote_average'],
                    vote_count=row['vote_count']
                )
