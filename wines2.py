from wine import Wine  # Наслідуємо клас Wine

class PackagedWine(Wine):
    def __init__(self, brand: str, description: str, strength: float, volume: float, container: str):
        #Ініціалізація фасованого вина з додатковими атрибутами: об’єм і тара
        super().__init__(brand, description, strength)
        self.__volume = volume  # Об'єм у літрах
        self.__container = container.lower()  # Тара: "скло" або "тетрапак"

    # Геттери
    def get_volume(self):
        return self.__volume

    def get_container(self):
        return self.__container

    # Сеттери
    def set_volume(self, volume):
        if volume <= 0:
            raise ValueError("Об'єм повинен бути більше 0!")
        self.__volume = volume

    def set_container(self, container):
        if container.lower() not in ["скло", "тетрапак"]:
            raise ValueError("Тара повинна бути 'скло' або 'тетрапак'!")
        self.__container = container.lower()

    def switch_container(self):
        #Змінює тару на протилежну
        self.__container = "скло" if self.__container == "тетрапак" else "тетрапак"

    def __truediv__(self, factor: float):
        #Перевантаження оператора '/' для зменшення об’єму у задану кількість разів
        if factor <= 0:
            raise ValueError("Фактор повинен бути більше 0!")
        new_volume = self.__volume / factor
        return PackagedWine(self.get_brand(), self.get_description(), self.get_strength(), new_volume, self.__container)

    def __str__(self):
        #Відображення фасованого вина у зручному форматі
        return f"{self.get_brand()} ({self.get_description()}) - {self.get_strength()}%, {self.__volume} л, тара: {self.__container}"
