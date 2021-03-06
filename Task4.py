class Car:

    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False
    ):

        self.color = color
        self.name = name
        self.is_police = True if is_police else False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):

        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):

        self.speed = 0

    def turn(self, direction: str):

        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"'Can't turn to {direction}' in place")
            return

        self._direction = direction

    def show_speed(self):

        print(f'My speed is {self.speed} km/h')

    @property
    def direction(self):

        return self._direction


class TownCar(Car):

    _max_granted_speed = 60

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class SportCar(Car):

    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    _max_granted_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Yellow', 'Aston Martin Cygnet'): TownCar,
        ('Green', 'BMW M3'): SportCar,
        ('White', 'VAZ 2106'): WorkCar,
        ('Red', 'Ford Crown Victoria'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('#######################################')
        print(f"Car name '{car.name}'")
        print(f"Car color '{car.color}'")
        print(f"Car is police '{car.is_police}'")
        print(f"Car speed '{car.speed}'")
        print(f"Car direction '{car.direction}'")
        print(f"Car show speed '{car.show_speed()}'")

        car.turn('right')
        car.turn('left')
        car.go(1)
        print("Car speed after invalid go", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Car direction '{car.direction}'")
        car.turn('right')
        print(f"Car direction '{car.direction}'")
        car.stop()
        car.show_speed()
        print('#######################################\n\n')
