from app import db

class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Coordinate(lat={self.lat}, long={self.long})"

class Waypoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    alt = db.Column(db.Float, nullable=False)
    flight_path_id = db.Column(db.Integer, db.ForeignKey('flight_path.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Waypoint(lat={self.lat}, long={self.long}, alt={self.alt})"

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    coordinates = db.relationship("Coordinate", backref="region", lazy=True)

    def __repr__(self) -> str:
        return f"Region(name={self.name}, coordinates={self.coordinates})"

class FlightPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"), nullable=False)
    region = db.relationship("Region", backref="flight_paths", lazy=True)
    waypoints = db.relationship("Waypoint", backref="flight_path", lazy=True)

    def __repr__(self) -> str:
        return f"FlightPath(name={self.name}, region={self.region.name}, waypoints={self.waypoints})"