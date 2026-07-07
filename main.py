import requests

API_KEY = "30724c017b063a23a0bcf2fa1a13c91a"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print("\n========== Weather Report ==========")
            print(f"City        : {data['name']}")
            print(f"Country     : {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']}%")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
            print("====================================")
        else:
            print("\nCity not found!")

    except Exception as e:
        print("Error:", e)


while True:
    city = input("\nEnter City Name (or 'exit'): ")

    if city.lower() == "exit":
        print("Thank you!")
        break

    get_weather(city)