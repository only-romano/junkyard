#! Файл класса для занятия Metanit, Глава 7, часть 1.


class Witness:

    # конструктор
    def __init__(self, name):
        self.name = name        # устанавливаем имя

    def display_witness(self):
        print("Привет, жертва, я знаю кто ты. Ты", self.name)


class Auto:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")
