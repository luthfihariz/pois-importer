import os
from unittest.mock import patch, call

from django.core.management import call_command, CommandError
from django.test import TestCase

from pois.domain import Poi, Coordinates
from pois.models import Poi as PoiModel


class ImportCommandTest(TestCase):
    def test_import_command_json_xml_csv(self):
        # Arrange    
        json_file = os.path.abspath("pois/tests/fixtures/test_pois.json")
        xml_file = os.path.abspath("pois/tests/fixtures/test_pois.xml")
        csv_file = os.path.abspath("pois/tests/fixtures/test_pois.csv")

        # Act
        call_command("import", json_file, xml_file, csv_file)

        # Assert
        self.assertEqual(PoiModel.objects.count(), 14)

        # Check the data for the JSON file
        json_pois = PoiModel.objects.filter(source_path=json_file)
        self.assertEqual(len(json_pois), 2)
        self.assertIsInstance(json_pois[0], PoiModel)

        # Check the data for the XML file
        xml_pois = PoiModel.objects.filter(source_path=xml_file)
        self.assertEqual(len(xml_pois), 2)
        self.assertIsInstance(xml_pois[0], PoiModel)

        # Check the data for the CSV file
        csv_pois = PoiModel.objects.filter(source_path=csv_file)
        self.assertEqual(len(csv_pois), 10)
        self.assertIsInstance(csv_pois[0], PoiModel)


    def test_import_unsupported_file(self):
        # Arrange
        file_path = os.path.abspath("pois/tests/fixtures/test_pois.txt")

        # Act
        with self.assertRaises(CommandError):
            call_command("import", file_path)

        # Assert
        self.assertEqual(PoiModel.objects.count(), 0)