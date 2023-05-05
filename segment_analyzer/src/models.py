from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from sqlalchemy.types import DateTime

db = SQLAlchemy()

class Effort(db.Model):
    __tablename__ = 'efforts' # new tablename
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    effort_id = db.Column(db.String(128), unique=True, nullable=False)
    effort_name = db.Column(db.String(128), nullable=False) 
    athlete_username = db.Column(db.String(128), nullable=False) 
    segment_name = db.Column(db.String(128), nullable=False) 
    segment_id = db.Column(db.Integer, nullable=False) 
    start_date_time = db.Column(db.DateTime, nullable=False) 
    elapsed_time = db.Column(db.Interval(), nullable=False) 
    moving_time = db.Column(db.Interval(), nullable=False) 
    effort_distance = db.Column(db.Float, nullable=False) 
    segment_distance = db.Column(db.Float, nullable=False) 
    average_watts = db.Column(db.Float, nullable=False) 
    average_heart_rate = db.Column(db.Float, nullable=False) 
    max_heart_rate = db.Column(db.Float, nullable=False) 
    wind_speed = db.Column(db.Float, nullable=False) 
    wind_direction = db.Column(db.Float, nullable=False)  