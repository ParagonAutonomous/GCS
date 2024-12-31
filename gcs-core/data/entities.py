"""Data structures for the GCS application."""
class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long
    
    def __repr__(self) -> str:
        return f"Coordinate(lat={self.lat}, long={self.long})"

class Waypoint(Coordinate):
    def __init__(self, lat: float, long: float, alt: float) -> None:
        super().__init__(lat, long)
        self.alt = alt

    def __repr__(self) -> str:
        return f"Waypoint(lat={self.lat}, long={self.long}, alt={self.alt})"

class Region:
    def __init__(self, name: str, coordinates: list[Coordinate]) -> None:
        self.name = name
        self.coordinates = coordinates
    
    def __repr__(self) -> str:
        return f"Region(name={self.name}, coordinates={self.coordinates})"
    
class FlightPath:
    def __init__(self, name: str, region: Region, waypoints: list[Waypoint]) -> None:
        self.name = name
        self.region = region
        self.waypoints = waypoints

    def __repr__(self) -> str:
        return f"FlightPath(name={self.name}, region={self.region.name}, waypoints={self.waypoints})"
