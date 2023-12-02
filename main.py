import sqlite3
import client
import Database
with sqlite3.connect("Касса") as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workers(
            workerID INTEGER PRIMARY KEY,
            Name VARCHAR(30) NOT NULL,
            Surname VARCHAR(30) NOT NULL,
            Middlename VARCHAR(30),
            Job VARCHAR(30) NOT NULL,
            Salary INTEGER NOT NULL,
            Age INTEGER NOT NULL,
            Email VARCHAR(50) NOT NULL,
            Password INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients(
            clientID INTEGER PRIMARY KEY,
            Name VARCHAR(30) NOT NULL,
            Surname VARCHAR(30) NOT NULL,
            Middlename VARCHAR(30),
            Age INTEGER NOT NULL,
            Email VARCHAR(50) NOT NULL,
            Password INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions(
            sessionID INTEGER PRIMARY KEY,
            Hours INTEGER NOT NULL,
            Cost INTEGER NOT NULL,
            Places INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cheque(
            chequeID INTEGER PRIMARY KEY,
            workerID INTEGER,
            clientID INTEGER,
            sessionID INTEGER,
            FOREIGN KEY (workerID) REFERENCES workers (workerID)
            FOREIGN KEY (clientID) REFERENCES clients (clientID)
            FOREIGN KEY (sessionID) REFERENCES sessions (sessionID)
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM workers")
    result = cursor.fetchone()[0]
    if result == 0:
        cursor.execute("INSERT INTO workers (workerID, Name, Surname, Middlename, Job, Salary, Age, Email, Password) values (1, \"Егор\", \"Прохоров\", \"Кириллович\", \"Кассир\", 25000, 26, \"EgProh@gmail.com\", \"Eg12#Proh\")")
    cursor.execute("SELECT COUNT(*) FROM sessions")
    result2 = cursor.fetchone()[0]
    if result2 == 0:
        data2 = [(1, 8.00 - 20.00, 2500, 50),
                 (2, 12.00 - 17.00, 1500, 50),
                 (3, 15.00 - 17.00, 800, 50)]
        cursor.executemany("INSERT INTO sessions (sessionID, Hours, Cost, Places) VALUES (?,?,?,?)", data2)
iD = 0
v = input("Добро пожаловать в наш компьютерный клуб! \nВпервые здесь? да/нет \n").lower()
match v:
    case "да":
        clientt = client.Client(0, "aa@gmail.com", "ffG%4", "а", "б", "в", 20)
        iD += 1
        n = input("Тогда давайте зарегестрируемся. Введите ваше имя. \n")
        clientt.name = n
        s = input("Введите вашу фамилию. \n")
        clientt.surname = s
        m = input("Введите ваше отчество. \n")
        clientt.middlename = m
        a = input("Введите ваш возраст. \n")
        clientt.age = a
        e = input("Введите вашу почту. \n")
        clientt.email = e
        p = input("Придумайте пароль. Он должен быть размером 8 символов, написан на латинице и содержать в себе хоть одно число и специальный символ. \n")
        clientt.password = p
        dataclient = {"clientID": iD, "Name": n, "Surname": s, "Middlename": m, "Age": a, "Email": e, "Password": p}
        with sqlite3.connect("Касса") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients(
                    clientID INTEGER PRIMARY KEY,
                    Name VARCHAR(30) NOT NULL,
                    Surname VARCHAR(30) NOT NULL,
                    Middlename VARCHAR(30),
                    Age INTEGER NOT NULL,
                    Email VARCHAR(50) NOT NULL,
                    Password INTEGER NOT NULL
                )
            ''')
            obj = Database.Database()
            obj.InsertData("clients", dataclient)
        print(f"Поздравляем с прохождением регистрации, {n}!")
    case "нет":
        u = " "
        while u != "":
            e = input("Введите вашу почту. \n")
            p = input("Введите пароль. \n")
            if e == "EgProh@gmail.com" and p == "Eg12#Proh":
                print("Добро пожаловать в систему, Егор Кириллович!")
                while True:
                    choise = input("Что нужно сделать? \nСоздать \nИзменить \nУдалить \nОтфильтровать").lower()
                    match choise:
                        case "создать":
                            table = input("В какой таблице вы хотите что-то создать? ")
                            column = input("В каком столбце? ")
                            value = input("Что хотите создать? ")
                            data = {column: value}
                            with sqlite3.connect("Касса") as conn:
                                cursor = conn.cursor()
                                obj = Database.Database()
                                obj.InsertData(table, data)
                        case "изменить":
                            table = input("В какой таблице вы хотите что-то изменить? ")
                            column = input("В каком столбце? ")
                            value = input("На что хотите изменить? ")
                            Id = input("Какое id у строки, в который вы хотите изменить данные?")
                            data = {column: value}
                            columnn = "".join([table, "ID"])
                            condition = {columnn: Id}
                            with sqlite3.connect("Касса") as conn:
                                cursor = conn.cursor()
                                obj = Database.Database()
                                obj.updatedata(table, data, condition)
                        case "удалить":
                            table = input("В какой таблице вы хотите что-то удалить? ")
                            Id = input("Какое id у строки, в который вы хотите удалить данные?")
                            columnn = "".join([table, "ID"])
                            condition = {columnn: Id}
                            with sqlite3.connect("Касса") as conn:
                                cursor = conn.cursor()
                                obj = Database.Database()
                                obj.deletedata(table, condition)
                        case "отфильтровать":
                            table = input("Какую таблицу вы хотите отфильтровать? ")
                            cond = input("По какому столбцу? ")
                            condi = input("Какому значению стобца? ")
                            condition = {cond: condi}
                            with sqlite3.connect("Касса") as conn:
                                cursor = conn.cursor()
                                obj = Database.Database()
                                obj.filterdata(table, condition)
                        case _:
                            print("Что-то пошло не так. Убедитесь в коректности вводимого запроса.")
            else:
                with sqlite3.connect("Касса") as conn:
                    cursor = conn.cursor()
                    cursor.execute(f'SELECT Name FROM clients WHERE Email = {e} AND Password = {p}')
                    n = cursor.fetchone()
                    if n == None:
                        print("Неправильный логин или пароль.")
                        u = " "
                    else:
                        u = ""
                    print(f"Добро пожаловать, {n}!")
    case _:
        print("Что-то пошло не так.")
with sqlite3.connect("Касса") as conn:
    cursor = conn.cursor()
    cursor.execute(f"SELECT Places FROM sessions WHERE sessionID=1")
    pl1 = cursor.fetchone()
    cursor.execute(f"SELECT Places FROM sessions WHERE sessionID=2")
    pl2 = cursor.fetchone()
    cursor.execute(f"SELECT Places FROM sessions WHERE sessionID=3")
    pl3 = cursor.fetchone()
print(
    f"Наш компьютерный клуб предлагает 3 разных пакета на выбор! \n1. С восьми утра до восьми вечера наш компьютер в вашем распоряжении всего за 2500! Свободных мест в зале: {pl1} \n2. 5 часов с полудня вы можете поиграть у нас за 1500! Свободных мест в зале: {pl2} \n3. 3 часа вечером за нашим компьютером за всего лишь 800 рублей! Свободных мест в зале: {pl3}")
xx = True
while xx == True:
    dn = input("Интересует что-нибудь? \n").lower()
    match dn:
        case "да":
            pac = input("1, 2, 3 пакет? \n")
            print("Прекрасно! На вашу почту пришла инструкция о том, как забронировать место в нашем зале на определённую дату по данному пакету вместе с контактами нашей службы поддержки.")
            xx = False
        case "нет":
            print("Очень жаль. Тогда до новых встреч! Мы всегда вам здесь рады.")
            xx = False
        case _:
            print("Что-то пошло не так. Убедитесь, что вы ввели либо да, либо нет.")