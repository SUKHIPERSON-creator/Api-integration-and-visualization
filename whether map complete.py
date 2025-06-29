import json
import requests
import matplotlib.pyplot as aakash

city = "Jaipur"
api_key = "ca58b976342514c5213956a6f8233625"  
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    Description =print(data['weather'][0]['description'])
    temperture =data['main']['temp']
    wind_speed=data['wind']['speed']
    humidity=data['main']['humidity']
labels=["temperture(°C)","wind_speed(m/s)","humidity(%)"]
values=[temperture,wind_speed,humidity]
aakash.bar(x=labels,height=values,color=['red','blue','green'])
aakash.title(f"weather of our {city}")
aakash.ylabel("values")
aakash.show()
