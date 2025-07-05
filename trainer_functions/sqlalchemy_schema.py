from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
db_url = 'sqlite:///trainer.db'
engine = create_engine(db_url)

Base = declarative_base()



class Foods(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)
    serving_g = Column(Float)
    date_added = Column(DateTime, default=datetime.now)
    @property
    def total_protein(self):
        return (self.protein * self.serving_g) / 100 if self.protein and self.serving_g else None

    @property
    def total_carbs(self):
        return (self.carbs * self.serving_g) / 100 if self.carbs and self.serving_g else None

    @property
    def total_fats(self):
        return (self.fats * self.serving_g) / 100 if self.fats and self.serving_g else None




class Trainings(Base):
    __tablename__ = 'training'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    weight = Column(Integer)
    reps = Column(Integer)
    date_added = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)
