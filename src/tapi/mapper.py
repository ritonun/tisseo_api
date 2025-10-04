# mapper.py

STATION_MAP = {
    "BASSO_COMBO": {"stop_area": "stop_area:SA_206", "index":0},
    "COMPANS-CAFARELLI": {"stop_area": "stop_area:SA_1072", "index": 1}
    # A COMPLETER
}


def get_station_area(station_name: str) -> str | None:
    """Renvoie l'id stopArea pour un nom de station"""
    station = STATION_MAP.get(station_name)
    if station:
        return station["stop_area"]
    else:
        return None


def get_station_index_from_area(stop_area: str) -> int | None:
    """Renvoie l'index de la station selon le stopArea"""
    for name, station in STATION_MAP.items():
        if station["stop_area"] == stop_area:
            return station["index"]
    return None
