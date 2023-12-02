import re
import client
class Worker(client):
    def __init__(self, salary, job):
        super().__init__()
        self.__salary = salary
        self.__job = job
    @staticmethod
    def jobValidate(value):
        pattern = r"^[а-яёА-ЯЁA-Za-z\]+$"
        return bool(re.match(pattern, value))
    @property
    def salary(self):
        return self.__salary
    @property
    def job(self):
        return self.__job
    @job.setter
    def job(self, value):
        if self.jobValidate(value):
            self.__job = value.capitalize()
        else:
            print("Недопустимое значение для должности")
    @salary.setter
    def salary(self, value):
        if self.ageValidate(value) and 16000 < value:
            self.__salary = value
        else:
            print("Зарплата меньше прожиточного минимума")
    def age(self, value):
        if self.ageValidate(value) and 16 < value < 120:
            self.__age = value
        else:
            while not self.ageValidate(value) and 16 < value < 120:
                print("Недопустимое значение для возраста")
                value = input("Введите ваш возраст. \n ")
                self.__age = value
