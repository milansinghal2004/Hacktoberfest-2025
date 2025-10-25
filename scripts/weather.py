import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        print(f"🌤️ {city} Weather: {response['main']['temp']}°C, {response['weather'][0]['description']}")
    else:
        print("❌ City not found")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)
