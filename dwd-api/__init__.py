import logging
from enum import Enum

logger = logging.getLogger('dwd-api')


class GeoType(Enum):
    """Enum representing geological location
    """
    BERG = 10    # mountain
    LAND = 20    # main land
    KUES = 30    # coast
    MEER = 40    # sea


class MosmixStation:
    """Class representing a station in mosmix format

    Attributes:
        metadata:   Metadata from msomix table
        id:         ID from mosmix station, at maximum 5 characters long
        name:       name of mosmix station
        clu:        ??? integer
        cofx:       ??? integer
        icao:       ??? 4 upper case letters or None
        latitude:   Original mosmix terminology: _nb._ : latutide of station.
        longitude:  Original mosmix terminology: _el._ : longitude of station
        elevation:  Original mosmix terminology: _elev_ : Height above sea level in meters
        hmod_h:     ??? integer
        geological_location:    GeoType
    """
    metadata: str
    id: str
    name: str
    clu: int
    cofx: int
    icao: str
    latitude: float     # moxmix_terminology: nb.
    longitude: float    # mosmix terminology: el.
    elevation: int      # moxmix termonology: elev
    hmod_h: int
    geological_location: GeoType







