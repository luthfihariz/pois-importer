import os
import time

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from pois.parsers.factory import ParserFactory
from pois.repository import PoiRepository


class Command(BaseCommand):
    help = "Import PoIs from one or more files"

    def add_arguments(self, parser):
        parser.add_argument(
            "files", nargs="+", type=str, help="The path to the file(s) to import."
        )

    def handle(self, *args, **options):
        start_time = time.time()
        for file_path in options["files"]:
            try:
                with transaction.atomic():
                    total_rows = self.process_file(file_path)
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully processed {total_rows} rows from file: {file_path}"
                    )
                )
            except Exception as e:
                raise CommandError(f"Error processing file '{file_path}': {e}")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished in {elapsed_time:.2f} seconds."
            )
        )

    def process_file(self, file_path: str) -> int:
        self.stdout.write(self.style.NOTICE(f"Processing file: {file_path}"))
        
        absolute_path = os.path.abspath(file_path)
        if not os.path.exists(absolute_path):
            raise CommandError(f"File not found: {file_path}")

        parser = ParserFactory.get_parser(absolute_path)
        poi_iterator = parser.get_poi_iterator(absolute_path)
        
        repository = PoiRepository()
        batch = []
        total_processed = 0

        for poi in poi_iterator:
            batch.append(poi)
            if len(batch) == 20000:
                processed_count = repository.bulk_create(batch)
                total_processed += processed_count
                self.stdout.write(f"  ...imported {total_processed} rows from {file_path}...")
                batch = []
        
        if batch:
            processed_count = repository.bulk_create(batch)
            total_processed += processed_count
            self.stdout.write(f"  ...imported {total_processed} rows from {file_path}...")

        return total_processed
