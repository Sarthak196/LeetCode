class Parking_lot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.parked_cars = {i: '' for i in range(1, total_slots+1)}

    def park_car(self, car):
        if self.available_slots > 0:
            for key in self.parked_cars:
                if self.parked_cars[key] == '':
                    slot_number = key
                    self.parked_cars[slot_number] = car.car_number
                    self.available_slots -= 1
                    return f"Car {car.car_number} parked successfully as slot {slot_number}."
        else:
            return "No available slots."

    def remove_car(self, car_number):
        for key in self.parked_cars:
            if self.parked_cars[key] == car_number:
                self.parked_cars[key] = ''
                self.available_slots += 1
                return f"Car {car_number} removed successfully from slot {key}."
        else:
            return f"Car {car_number} not found in the parking lot."

    def get_available_slots(self):
        return self.available_slots

    def __str__(self):
        return f"Parking Lot: {self.parked_cars}"

class Car:
    def __init__(self, car_number):
        self.car_number = car_number

    def __str__(self):
        return f"Car Number: {self.car_number}"

def main():
    parking_lot = Parking_lot(3)

    while True:
        print("\n1. Park Car")
        print("2. Remove Car")
        print("3. Check Available Slots")
        print("4. Get Parking Lot Status")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_number = input("Enter car number: ")
            car = Car(car_number)
            print(parking_lot.park_car(car))

        elif choice == '2':
            car_number = input("Enter car number to remove: ")
            print(parking_lot.remove_car(car_number))

        elif choice == '3':
            print(f"Available slots: {parking_lot.get_available_slots()}")

        elif choice == '4':
            print(parking_lot)

        elif choice == '5':
            print("Exiting the parking system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()