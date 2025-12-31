class Car:
    def __init__(self, model, fuel, fuel_consumption):
        self.model = model
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'{self.model}: tank - {self.fuel}L, consumption - {self.fuel_consumption}L/100KM'

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        if int(fuel) < 0:
            self._fuel = 0
            print("=====ERROR FUEL CAN'T BE NEGATIVE=====")
        else:
            self._fuel = int(fuel)

class Fleet:
    def __init__(self):
        self._cars = []

    def add_car(self, car):
        if car not in self._cars:
            self._cars.append(car)
            print(f"{car} added in fleet")
        else:
            print("=====CAR ALREADY IN FLEET=====")

    def send_on_trip(self, index, distance):
        try:
            idx = int(index)

            car = self._cars[idx]

            fuel_need = (distance * car.fuel_consumption) / 100
            if fuel_need > car.fuel:
                print("=====NOT ENOUGH FUEL=====")
            else:
                car.fuel -= fuel_need
                print(f"=====SUCCESS: {car.model} left {car.fuel}L=====")

        except (ValueError, IndexError):
            print("===== ERROR: INVALID CAR INDEX =====")

    def refuel_all(self,liters):
        if liters <= 0:
            print("=====ERROR=====")
        else:
            for i in self._cars:
                i.fuel += liters
                print(f"CARS FILLED UP ON {liters} LITERS")

    def view_cars(self):
        for i, n in enumerate(self._cars):
            print(f"{i + 1}. {n.model}: {n.fuel}L left, index:{i}")

    def remove_car(self, index):
        try:
            idx = int(index)

            car = self._cars.pop(idx)
            print(f"{car.model} removed in fleet")

        except (ValueError, IndexError):
            print("===== ERROR: INVALID CAR INDEX =====")



def main():
    toyota = Car("Toyota", 50, 8)
    ford = Car("Ford", 40, 12)

    myfleet = Fleet()

    myfleet.add_car(toyota)
    myfleet.add_car(ford)

    while True:
        print("=====MAIN MENU=====")
        print("1.CREATE CAR AND ADD ON FLEET", "\n2.SEND ON A TRIP CARS", "\n3.REFUEL CARS", "\n4.VIEW CARS", "\n5.REMOVE CAR", "\n6.EXIT")

        choice = int(input("CHOICE THE NUMBER(1-6): "))
        if choice == 1:
            model = input("ENTER MODEL: ")
            fuel = input("ENTER FUEL(LITERS): ")
            fuel_consumption = input("ENTER FUEL CONSUMPTION(LITERS/100KM): ")
            myfleet.add_car(Car(model, fuel, fuel_consumption))
        elif choice == 2:
            index = input("ENTER INDEX CAR(view cars): ")
            try:
                distance = int(input("ENTER DISTANCE CAR(KM): "))
            except ValueError:
                print("=====ERROR=====")
                distance = 0
            myfleet.send_on_trip(index, distance)
        elif choice == 3:
            try:
                fuel = int(input("ENTER FUEL(LITERS): "))
            except ValueError:
                print("=====ERROR=====")
                fuel = 0
            myfleet.refuel_all(fuel)

        elif choice == 4:
            myfleet.view_cars()

        elif choice == 5:
            try:
                index = int(input("ENTER INDEX CAR(view cars): "))
            except ValueError:
                print("=====ENTER CORRECT INDEX=====")
            myfleet.remove_car(index)

        elif choice == 6:
            break

        else:
            print("=====ENTER VALID CHOICE=====")


if __name__ == "__main__":
    main()