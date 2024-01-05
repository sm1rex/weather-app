from crypt import methods
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "e82004a955b605fe7e31b65cb979a97e"

        url = BASE_URL + "q=" + city_name + "&units=metric&APPID=" + API_KEY
        print(url)
        response = requests.get(url).json()

        weather = response['weather'][0]['main']
        temp = response['main']['temp']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']


        return render_template('index.html', city = city_name, temperature = temp, min_temperature = min_temp, max_temperature = max_temp, pressure = pressure, humidity = humidity)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()