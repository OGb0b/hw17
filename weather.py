from dotenv import load_dotenv
import os
import requests



load_dotenv(os.path.join(os.path.dirname(__file__), './config/.env'))

class Weather:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL")

    def current_weather(self, city):
        url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric&lang=ru"

        try:
            response = requests.get(url, timeout=5)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP ошибка: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Ошибка подключения. Проверьте интернет-соединение.")
        except requests.exceptions.Timeout:
            print("Запрос превысил время ожидания.")
        except requests.exceptions.RequestException as err:
            print(f"Произошла ошибка: {err}")

        return response.json()
