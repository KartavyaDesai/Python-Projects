#Desktop Notifier
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Function to fetch data
def data(url):
    r = requests.get(url)
    return r.text
x = data("https://weather.com/en-IN/weather/today/l/5586e95f0af9435d00bc0a636eb9a059c81f4851e32102d3eb0ca3df6b2428fe")
soup = BeautifulSoup(x, 'html.parser')

temp = str(soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY"))
aqi = str(soup.find_all("span", class_="AirQualityText--severity--W9CtX"))
#Identifying the index of the data i need.
start_index_aqi = aqi.find('Moderate')
print(start_index_aqi)

start_index_temp = temp.find('21')
print(start_index_temp)
# print(temp[82:84], aqi[80:88])

#Creating Notfier Object
notification = "Current Temprature :" + temp[82:84] + " Celcius\n" + "AQI Level: " + aqi[80:88]
notice = ToastNotifier()
notice.show_toast("Weather Update", notification, duration=10)