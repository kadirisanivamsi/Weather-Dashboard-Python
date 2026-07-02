from weather import get_weather
from history import save_history, show_history

while True:
    print("\n==============================")
    print("     WEATHER DASHBOARD")
    print("==============================")
    print("1. Search Weather")
    print("2. View Search History")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        city = input("Enter City Name: ")

        data = get_weather(city)

        if data:
            save_history(city)

            print("\nWeather Details")
            print("---------------------------")
            print(f"City        : {data['name']}")
            print(f"Country     : {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']} %")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
        else:
            print("❌ City not found.")

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Thank you for using Weather Dashboard!")
        break

    else:
        print("Invalid choice. Please try again.")