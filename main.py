from gpiozero import LED
import psutil
import time
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation
import Adafruit_DHT
import pandas as pd
sensor1= Adafruit_DHT.DHT11
pin = 20
led_yellow = LED(5)
led_green = LED(6)
led_red = LED(14)
ultrasonic = DistanceSensor(echo=17, trigger=4)

h,t = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

log_file = open("test.csv", "a")
while True:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    distance= ultrasonic.distance
    if t is not None and h is not None:
        log_file.write(t,h,distance,timestamp)
        print(f"the temp = {t}, the humidity = {h}, the distance = {distance}")
    else:
        print("there is error in reading the values")
log_file.close()
data = pd.read_csv(log_file, names=['Timestamp', 'Temperature', 'Humidity', 'Distance'])
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Temperature'], label='Temperature (°C)', color='red', marker='o')
plt.plot(data['Timestamp'], data['Humidity'], label='Humidity (%)', color='blue', marker='o')
plt.plot(data['Timestamp'], data['Distance'], label='Distance (cm)', color='green', marker='o')
plt.title('Sensor Data Over Time')
plt.xlabel('Time')
plt.ylabel('Readings')
plt.legend()
plt.xticks(rotation=45)
plt.savefig("sensor_data_plot.png")
ani = FuncAnimation(fig, update, interval=100)
plt.show()
