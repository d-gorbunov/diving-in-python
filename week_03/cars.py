# Реализация иерархии классов автомобилей

import os
import csv


class CarBase:
    required = []

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self._validate_input(brand)
        self.carrying = float(self._validate_input(carrying))
        self.photo_file_name = self._validate_photo_file_name(photo_file_name)

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

    def _validate_input(self, data):
        if data == '':
            raise ValueError
        return data

    def _validate_photo_file_name(self, filename):
        for ext in ('.jpeg', '.jpg', '.gif', '.png'):
            if filename.endswith(ext) and len(filename) > len(ext):
                return filename
        raise ValueError


    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            length, width, height = body_whl.split('x')
            length, width, height = float(length), float(width), float(height)
        except Exception:
            length, width, height = 0.0, 0.0, 0.0
        self.body_length, self.body_width, self.body_height = length, width, height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'extra']

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r', newline='') as fp:
        reader = csv.reader(fp, delimiter=';')
        for row in reader:
            print(row)
    return car_list


if __name__ == '__main__':
    print(get_car_list('cars.csv'))
