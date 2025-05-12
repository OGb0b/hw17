class Data:
    def avg_temp(self, data):
        average_temperature = 0
        for city_weather in data:
            average_temperature += city_weather['temperature']
        return average_temperature / len(data)

    def max_temp(self, data):
        max_temperature = [0, data[0]['city']]
        for city_weather in data:
            if city_weather['temperature'] > max_temperature[0]:
                max_temperature = [city_weather['temperature'],city_weather['city']]
        return max_temperature

    def min_temp(self, data):
        min_temperature =  [data[0]['temperature'], data[0]['city']]
        for i in range(1, len(data)):
            if data[i]['temperature'] < min_temperature[0]:
                min_temperature = [data[i]['temperature'], data[i]['city']]
        return min_temperature

