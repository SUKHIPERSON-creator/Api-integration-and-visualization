import json
import requests
# requet  library is used for use the database or internet
import matplotlib.pyplot as aakash
# This library is used for making a bar graph

city = "Jaipur"
api_key = "ca58b976342514c5213956a6f8233625"  
#It is provided by 'Openwhethermap'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  

response = requests.get(url)
#get permission to use the data base 

if response.status_code == 200:
    #for checking our code 
    data = response.json()
    #data is variable that store  response in json format
    # slicing part to get useful data form data base 
    Description =print(data['weather'][0]['description'])
    temperture =data['main']['temp']
    wind_speed=data['wind']['speed']
    humidity=data['main']['humidity']
    #ploting a graph
labels=["temperture(°C)","wind_speed(m/s)","humidity(%)"]
values=[temperture,wind_speed,humidity]
aakash.bar(x=labels,height=values,color=['red','blue','green'])
aakash.title(f"weather of our {city}")
aakash.ylabel("values")
aakash.show()
