import re
class Client():
    def __init__(self, id, email, password, name, surname, middlename, age):
        self.__id = id
        self.__email = email
        self.__password = password
        self.__name = name
        self.__surname = surname
        self.__middlename = middlename
        self.__age = age
    @staticmethod
    def fioValidate(value):
        cyrillic = "^[а-яёА-ЯЁ\-]+$"
        return bool(re.match(cyrillic, value))
    @staticmethod
    def ageValidate(value):
        brilliancy = "1234567890"
        for char in value:
            if char in brilliancy:
                return True
            else:
                return False
    @staticmethod
    def emailValidate(value):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return bool(re.match(pattern, value))
    @staticmethod
    def passwordValidate(value):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        return bool(re.match(pattern, value))
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if self.fioValidate(value):
            self.__name = value.capitalize()
        else:
            while not self.fioValidate(value):
                print("Недопустимое значение для имени")
                value = input("Введите имя. \n")
                self.__name = value.capitalize()
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value):
        if self.fioValidate(value):
            self.__surname = value.capitalize()
        else:
            while not self.fioValidate(value):
                print("Недопустимое значение для фамилии")
                value = input("Введите фамилию. \n")
                self.__surname = value.capitalize()
    @property
    def middlename(self):
        return self.__middlename
    @middlename.setter
    def middlename(self, value):
        if self.fioValidate(value):
            self.__middlename = value.capitalize()
        else:
            while not self.fioValidate(value):
                print("Недопустимое значение для отчества")
                value = input("Введите отчество. \n")
                self.__middlename = value.capitalize()
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if self.ageValidate(value):
            self.__age = value
        else:
            while not self.ageValidate(value):
                print("Недопустимое значение для возраста")
                value = input("Введите ваш возраст. \n ")
                self.__age = value
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        if self.emailValidate(value):
            self.__email = value
        else:
            while not self.emailValidate(value):
                print("Недопустимое значение для email")
                value = input("Введите вашу почту. \n ")
                self.__email = value
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if self.passwordValidate(value):
            self.__password = value
        else:
            while not self.passwordValidate(value):
                print("Пароль не соответствует требованиям")
                value = input("Придумайте пароль. Он должен быть размером 8 символов, написан на латинице и содержать в себе хоть одно число и специальный символ. \n")
                self.__password = value
