import os
import datetime
from sqlalchemy.orm import sessionmaker
from models import WeatherData, engine

Session = sessionmaker(bind=engine)
session = Session()

def ingest_data(file_path):
    station_id = os.path.basename(file_path).split('.')[0]
    with open(file_path, 'r') as file:
        for line in file:
            data = line.split('\t')
            date = datetime.datetime.strptime(data[0], '%Y%m%d')
            max_temp = None if data[1] == '-9999' else int(data[1]) / 10
            min_temp = None if data[2] == '-9999' else int(data[2]) / 10
            precipitation = None if data[3] == '-9999' else int(data[3]) / 10

            weather_data = WeatherData(station_id=station_id, date=date, max_temp=max_temp, min_temp=min_temp, precipitation=precipitation)
            session.merge(weather_data)

    session.commit()

