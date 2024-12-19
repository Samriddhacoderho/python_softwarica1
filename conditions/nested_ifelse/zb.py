weather = input("Enter the weather (sunny/rainy): ").lower()

if weather == "sunny":
    print("Recommended activities: hiking or a picnic.")
elif weather == "rainy":
    rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if rain_gear == "yes":
        print("Recommended activities: going to a nearby mall or museum.")
    else:
        print("Recommended activities: staying home and watching movies.")
else:
    print("Invalid weather input.")
