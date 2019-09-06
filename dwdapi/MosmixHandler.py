from . import logger
from . import MosmixStation
from typing import List, Dict
import csv


class MosmixHandler:

    @staticmethod
    def open_mosmix_file(input_file: str) -> List[list]:
        """Opens mosmix station file

        :param input_file:
        :return:
        """
        with open(input_file, 'r', encoding='utf-8') as mosmix_station_file:
            list_of_stations: List[list] = []
            stations: List[MosmixStation] = []
            for line in mosmix_station_file:
                if not line.strip():
                    metadata: str = None
                    column_specs: Dict[str, int] = {}
                    headers: List[str] = {}
                    if stations:
                        list_of_stations.append(stations)
                        stations: List[MosmixStation] = []
                elif line.startswith('TABLE'):
                    metadata = line
                elif line.startswith('clu'):
                    headers = line.split()
                elif line.startswith('=='):
                    column_specs = MosmixHandler._create_column_specs(headers, line)
                else:
                    station = MosmixHandler._create_mosmix_station_from_line(column_specs, line)
                    if station:
                        station.metadata = metadata
                        stations.append(station)
                    else:
                        logger.warn('Could not read station from line:\n%s' % line)
            return list_of_stations

    @staticmethod
    def _create_column_specs(headers: List[str], line: str) -> Dict[str, int]:
        """Create a mapping of column name and column length

        :param headers:
        :param line:
        :return:
        """
        column_specs: Dict[str:int] = {}
        column_length_counters = line.split()
        for i in range(len(headers)):
            column_specs[headers[i]] = len(column_length_counters[i])
        return column_specs

    @staticmethod
    def _create_mosmix_station_from_line(column_specs, line) -> MosmixStation:
        """Creates a new mosmix station from a line

        :param column_specs:
        :param line:
        :return:
        """
        start_index = 0
        new_station = MosmixStation()
        for column_name, column_length in column_specs.items():
            column_end = start_index + column_length
            if 'nb.' is column_name:
                new_station.latitude = line[start_index:column_end].strip()
            elif 'el.' is column_name:
                new_station.longitude = line[start_index:column_end].strip()
            elif 'elev' is column_name:
                new_station.elevation = line[start_index:column_end].strip()
            else:
                setattr(new_station, column_name, line[start_index:column_end].strip())
            start_index += column_length + 1
        return new_station

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