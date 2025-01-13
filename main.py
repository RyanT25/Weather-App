
#! Weather App

#* Weather Data
weather_data = { 
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} 
}

#* Welcome Message
print("--------------------")
print("Welcome to the 'City Weather App'! ")
print("--------------------")
print("Cities Available: "+", ".join(weather_data.keys()))
#* User Input
user_city_input = input("Enter City Name: ")
print("--------------------")

#* Display Weather Data
"""
def display_data(user_city_input):
    print(f"Current Weather In, {user_city_input}:")
    print(f"Temperature: {weather_data[user_city_input]         ["temperature"]}")
    print(f"Conditions: {weather_data[user_city_input]["conditions"]}")
    print(f"Wind Speed: {weather_data[user_city_input]["wind_speed"]}")
    print(f"Humidity: {weather_data[user_city_input]["humidity"]}")
display_data(user_city_input)

"""
#* Data Validation
def display_data(user_city_input):
    while True:
        if user_city_input in weather_data:
            print(f"Current Weather In, {user_city_input}:")
            print(f"Temperature: {weather_data[user_city_input]['temperature']}")
            print(f"Conditions: {weather_data[user_city_input]['conditions']}")
            print(f"Wind Speed: {weather_data[user_city_input]['wind_speed']}")
            print(f"Humidity: {weather_data[user_city_input]['humidity']}")
            print("--------------------")
            break
        else:
            print("Invalid Input - Please Try Again!")
            user_city_input = input("Enter City Name: ")
            print("--------------------")
display_data(user_city_input)

#* Thank You Message
print("Thank you for using the 'City Weather App'! \n")
