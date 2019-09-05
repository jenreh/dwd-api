from . import logger
from . import MosmixStation
from typing import List
import csv


class MosmixHandler:

    def mosmix_to_csv(self, input_file: str, output_file: str):
        """Reads data from mosmix station file and converts it to csv

        """
        raise NotImplementedError

    def mosmix_to_dicts(self, input_file: str):
        """Reads stations from a mosmix input file and returns list of dictionaries.

        :param input_file:
        :return: list of dictionaries
        """
        raise NotImplementedError

    def csv_to_mosmix(self, input_file: str, output_file: str):
        """Reads stations from csv file and write it to mosmix file.

        :param input_file:
        :param output_file:
        """
        raise NotImplementedError

    @staticmethod
    def _import_mosmix_file(self, input_file: str, reset: bool = True):
        """Write mosmix station to a local database.

        :param input_file: path to mosmix file
        :param reset: If True, database is reset.
        :return:
        """
        raise NotImplementedError

    def import_mosmix(self, input_files: List[str], reset: bool = True):
        """Writes mosmix files to database.

        :param input_files:
        :param reset:
        :return:
        """
        raise NotImplementedError