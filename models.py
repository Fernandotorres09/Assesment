from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    station_id = Column(String)
    date = Column(Date)
    max_temp = Column(Integer)
    min_temp = Column(Integer)
    precipitation = Column(Integer)

class WeatherStats(Base):
    __tablename__ = 'weather_stats'

    id = Column(Integer, primary_key=True)
    station_id = Column(String)
    year = Column(Integer)
    avg_max_temp = Column(Integer)
    avg_min_temp = Column(Integer)
    total_precipitation = Column(Integer)

engine = create_engine('postgresql://postgres:1998@localhost:5432/weather_api')
Base.metadata.create_all(engine)
