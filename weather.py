weather_data = {
  "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
  "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "58%"}, 
  "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
  "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
  "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} 
}

def display_welcome(): 
    print("Welcome to the Weather Forecast App!") 
def get_city(): 
    city = input("Enter the city name for the weather forecast: ") 
    return city

def display_weather(city):
    if city in weather_data:
      print(f"Weather in {city}:") 
      print(f"Temperature: {weather_data[city]['temperature']}")
      print(f"Conditions: {weather_data[city]['conditions']}") 
      print(f"Wind Speed: {weather_data[city]['wind_speed']}") 
      print(f"Humidity: {weather_data[city]['humidity']}") 
    else:
      print("Sorry, the city is not in our database. Please try again.") 
      
def get_valid_city():
    while True:
        city = get_city() 
        if city in weather_data:
            return city 
        else: 
            print("Invalid city. Please try again.") 
  
def display_thank_you():
    print("Thank you for using the Weather Forecast App!") 

def main(): 
    display_welcome()
    city = get_valid_city()
    display_weather(city)
    display_thank_you() 

if __name__ == "__main__":
    main()
