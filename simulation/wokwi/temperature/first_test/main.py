"""
First terrarium sensor test using DHT22 temperature/humidity sensor
Tests basic sensor reading and output formatting
"""
from machine import Pin
from dht import DHT22
from time import sleep

# Initialize the DHT22 sensor
sensor = DHT22(Pin(15))ls

def read_sensor():
    """Read temperature and humidity from DHT22 sensor"""
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        return temperature, humidity
    except Exception as e:
        print('Error reading sensor:', str(e))
        return None, None

def main():
    """Main program loop"""
    print("Terrarium Environment Monitor Starting...")
    print("Reading DHT22 sensor every 2 seconds...")
    
    while True:
        temp, hum = read_sensor()
        if temp is not None and hum is not None:
            print(f"Temperature: {temp:.1f}°C")
            print(f"Humidity: {hum:.1f}%")
        print("-" * 20)
        sleep(2)

if __name__ == "__main__":
    main()