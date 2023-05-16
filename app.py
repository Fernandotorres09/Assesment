from flask import Flask
from flask_restful import Api, Resource
from sqlalchemy import func, create_engine
from models import WeatherData, WeatherStats
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
api = Api(app)

# Add the following code
engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)
session = Session()

class WeatherResource(Resource):
    def get(self):
        data = session.query(WeatherData).all()
        return [{ 'station_id': d.station_id, 'date': d.date, 'max_temp': d.max_temp, 'min_temp': d.min_temp, 'precipitation': d.precipitation } for d in data]

class WeatherStatsResource(Resource):
    def get(self):
        stats = session.query(WeatherStats).all()
        return [{ 'station_id': s.station_id, 'year': s.year, 'avg_max_temp': s.avg_max_temp, 'avg_min_temp': s.avg_min_temp, 'total_precipitation': s.total_precipitation } for s in stats]

api.add_resource(WeatherResource, '/api/weather')
api.add_resource(WeatherStatsResource, '/api/weather/stats')

if __name__ == '__main__':
    app.run(debug=True)