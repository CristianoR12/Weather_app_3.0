from flask import Blueprint, render_template, request
from weather_buddy.models import City
from . import db, API_key
import requests

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

@views.route('/weather', methods=['GET', 'POST'])
def home():   

    if request.method == 'POST':        
        new_city = request.form.get('city')

        if new_city:
            city_obj = City(name=new_city)

            db.session.add(city_obj)
            db.session.commit()           

    url = f'http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=imperial&appid={API_key}'
      
    Response = requests.get(url)
    data = Response.json()
    
    weather_data = {
        'city' : new_city,
        'temperature' : data['main']['temp'],
        'description' : data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    
    return render_template('weather.html', weather=weather_data)               

