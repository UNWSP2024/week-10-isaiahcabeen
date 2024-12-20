class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

my_car = Car(2024, "Toyota")

for _ in range(5):
    my_car.accelerate()
    print(f"Current speed after accelerating: {my_car.get_speed()}")

for _ in range(5):
    my_car.brake()
    print(f"Current speed after braking: {my_car.get_speed()}")
