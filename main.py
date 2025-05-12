import weather
from hw17 import analysis_data
import pandas as pd


data = []
conn = weather.Weather()
cities = ['Moscow', 'New York', 'Tokyo', 'London', 'Berlin']

for city in cities:
    city_weather = conn.current_weather(city)
    temp = city_weather['main']['temp']
    humidity = city_weather['main']['humidity']
    wind_speed = city_weather['wind']['speed']
    description = city_weather['weather'][0]['description']
    city_weather_data = {
        'city' : city,
        'temperature' : temp,
        'humidity' : humidity,
        'wind_speed' : wind_speed,
        'description' : description
    }
    data.append(city_weather_data)


final_data = analysis_data.Data()
average_temperature = final_data.avg_temp(data)
max_temperature = final_data.max_temp(data)
min_temperature = final_data.min_temp(data)

print(f'Средняя температура городов - {str(average_temperature)[:4]}',
      f'Максимальная температура в городе - {max_temperature[1]}, температура  - {max_temperature[0]}',
      f'Минимальная температура в городе - {min_temperature[1]}, температура  - {min_temperature[0]}', sep='\n')

df = pd.DataFrame(data)
df.to_csv(
    'weather_report.csv',
    index=False,
    sep=',',
    encoding='utf-8',
    header=True
)
print("Данные сохранены в weather_report.csv")