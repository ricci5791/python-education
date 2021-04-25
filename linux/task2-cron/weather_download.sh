#! usr/bin/bash

cd $HOME && curl -o weather_forecast.json http://api.openweathermap.org/data/2.5/weather?q=Kiev&appid=d370eeb23d0eb74a83a12f6b2596e0b5 > $HOME/weather.json
