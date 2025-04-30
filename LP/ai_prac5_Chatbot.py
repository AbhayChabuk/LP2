def show_new_cars(body_type, brand_filter=None):
    cars = {
        "sedan": ["Toyota Camry", "Honda Accord", "Hyundai Elantra"],
        "suv": ["Toyota RAV4", "Ford Escape", "Honda CR-V"],
        "all": ["Toyota Camry", "Honda Accord", "Hyundai Elantra",
                "Toyota RAV4", "Ford Escape", "Honda CR-V"]
    }

    print(f"\nAvailable NEW {body_type.upper()} Cars:")
    found = False
    for car in cars.get(body_type, []):
        if brand_filter and brand_filter.lower() not in car.lower():
            continue
        print("•", car)
        found = True

    if not found:
        print("No cars found for that brand.")

def show_used_cars(budget, year_filter=None, mileage_filter=None, brand_filter=None):
    used_cars = [
        {"name": "2017 Toyota Corolla", "price": 8000, "year": 2017, "mileage": 65000},
        {"name": "2018 Honda Civic", "price": 9000, "year": 2018, "mileage": 60000},
        {"name": "2015 Ford Focus", "price": 5000, "year": 2015, "mileage": 85000},
        {"name": "2016 Nissan Altima", "price": 7000, "year": 2016, "mileage": 72000}
    ]

    print(f"\nSearching USED cars under ${budget}")
    found = False
    for car in used_cars:
        if car["price"] > budget:
            continue
        if year_filter and car["year"] < year_filter:
            continue
        if mileage_filter and car["mileage"] > mileage_filter:
            continue
        if brand_filter and brand_filter.lower() not in car["name"].lower():
            continue
        print(f"• {car['name']} (${car['price']}, {car['year']}, {car['mileage']} miles)")
        found = True

    if not found:
        print("No used cars matched your filters.")

def chatbot():
    print("Welcome to the Ultimate Car Finder Chatbot!")
    name = input("May I know your name?\n> ").strip().title()
    print(f"\nHi {name}! How can I assist you today?")

    while True:
        print("\nMAIN MENU:")
        print("1. Find a Car")
        print("3. About")
        print("4. Exit")
        choice = input("> ").lower().strip()

        if choice == "1" or "find" in choice:
            while True:
                print("\nAre you looking for a New or Used car? (type 'back' to return)")
                car_type = input("> ").lower().strip()
                if car_type == "back":
                    break
                elif car_type == "new":
                    print("What body type? (Sedan, SUV, All)")
                    body_type = input("> ").lower().strip()
                    print("Filter by brand? (Toyota, Honda, etc. or press Enter to skip)")
                    brand_filter = input("> ").lower().strip()
                    show_new_cars(body_type, brand_filter)

                elif car_type == "used":
                    print("What's your maximum budget?")
                    budget_input = input("> ").strip()
                    if not budget_input.isdigit():
                        print("Invalid budget input.")
                        continue
                    budget = int(budget_input)

                    print("Minimum Year? (e.g. 2016 or press Enter to skip)")
                    year_input = input("> ").strip()
                    year_filter = int(year_input) if year_input.isdigit() else None

                    print("Max Mileage? (e.g. 70000 or press Enter to skip)")
                    mileage_input = input("> ").strip()
                    mileage_filter = int(mileage_input) if mileage_input.isdigit() else None

                    print("Filter by brand? (e.g. Toyota or press Enter to skip)")
                    brand_filter = input("> ").strip()
                    show_used_cars(budget, year_filter, mileage_filter, brand_filter)

                else:
                    print("Please type 'new' or 'used'.")

        elif choice == "3" or "about" in choice:
            print("\nAbout Us:")
            print("We help you find the best new or used cars.")
            print("Filters include type, brand, budget, mileage, and year!")

        elif choice == "4" or "exit" in choice:
            print(f"\nThanks for visiting, {name}! Safe driving!")
            break

        else:
            print("Please select a valid option from the menu.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
