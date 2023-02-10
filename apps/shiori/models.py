from apps.app import db

class Itinerary(db.Model):
    __tablename__ = "Itinerarys"
    id = db.Column(db.Integer, primary_key=True)
    itinerary = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)