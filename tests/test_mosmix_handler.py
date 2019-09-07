import unittest
from dwdapi.MosmixHandler import MosmixHandler


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_open_mosmix_file(self):
        list_of_stations = MosmixHandler.open_mosmix_file('./tests/resources/mosmix_stations.txt')
        assert 0 < len(list_of_stations)

        for station_list in list_of_stations:
            if station_list:
                for station in station_list:
                    assert None is not station.name, 'Station has no name:\t%s' % station
                    assert None is not station.metadata, 'Station has no metadata:\t%s' % station.name
                    print(f'{station.id}\t{station.name}\t{station.type}')


if __name__ == '__main__':
    unittest.main()
