import datetime


class Car:

    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('RUN')


class ToyotaCar(Car):

    def run(self):
        print('ToyotaCAR_RUN')


car = Car('Nomal Car')
print(car.model)
car.run()

toyotacar = ToyotaCar('Lexus')
print(toyotacar.model)
toyotacar.run()


class Country:

    def __init__(self, country_name):
        self.country_name = country_name


class City(Country):

    def __init__(self, country_name, city_name):
        super().__init__(country_name)
        self.city_name = city_name


japan = City('Japan', 'Tokyo')
print(japan.country_name)
print(japan.city_name)


# class TestClass:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # インスタンスメソッド
#     def sample_instancemethod(self, display_x=True, display_y=True):
#         if display_x:
#             print(f'x is {self.x}')
#         if display_y:
#             print(f'f is {self.y}')


# test_class1 = TestClass(100, 50)
# test_class1.sample_instancemethod(display_x=False)


class TestClass:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return cls(d.year, d.month, d.day)

    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(x, y):
        return x + y


# インスタンス化せずに呼び出す
test_class_1 = TestClass.sample_classmethod()
print(test_class_1.year, test_class_1.month, test_class_1.day)

# インスタンス化せずに呼び出す
test_class_2 = TestClass.sample_classmethod(-10)
print(test_class_2.year, test_class_2.month, test_class_2.day)

# 通常のインスタンス
test_class_3 = TestClass(2000, 1, 1)
print(test_class_3.year, test_class_3.month, test_class_3.day)

# インスタンス化せずに呼び出す
print(TestClass.sample_staticmethod(10, 100))

# インスタンス化してから呼び出す
test_class_4 = TestClass(2000, 1, 1)
print(test_class_4.sample_staticmethod(100, 1000))
