from wine_collection import WineCollection
class WineCollection:
    def __init__(self):
        #Створює колекцію фасованих вин
        self.__wines = []

    def add_wine(self, wine: PackagedWine):
        #Додає фасоване вино до списку
        if not isinstance(wine, PackagedWine):
            raise TypeError("Можна додавати тільки об'єкти класу PackagedWine")
        self.__wines.append(wine)

    def load_from_file(self, filename: str):
        #Завантажує вина з текстового файлу у форматі: Назва:Опис:Міцність:Об'єм:Тара
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(":")
                    if len(parts) != 5:
                        print(f"Некоректний формат рядка: {line.strip()}, пропускаємо...")
                        continue
                    brand, description, strength, volume, container = parts
                    wine = PackagedWine(brand, description, float(strength), float(volume), container)
                    self.add_wine(wine)
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")

    def display_wines(self):
        #Відображає список вин за спаданням міцності
        sorted_wines = sorted(self.__wines, key=lambda wine: wine.get_strength(), reverse=True)
        for wine in sorted_wines:
            print(wine)

    def total_volume_by_color(self):
        #Розраховує загальний об’єм вин кожного кольору (біле, червоне, рожеве)
        volumes = {"біле": 0.0, "червоне": 0.0, "рожеве": 0.0}
        for wine in self.__wines:
            for color in volumes:
                if color in wine.get_description().lower():
                    volumes[color] += wine.get_volume()
        for color, volume in volumes.items():
            print(f"Загальний об'єм {color} вина: {volume:.2f} л")
            
from wine_collection import WineCollection

# Створення колекції вин
collection = WineCollection()

# Додавання вин вручну
collection.add_wine(PackagedWine("Сапераві", "червоне сухе", 14.0, 0.75, "скло"))
collection.add_wine(PackagedWine("Рислінг", "біле напівсолодке", 9.5, 1.0, "тетрапак"))

# Завантаження вин з файлу
collection.load_from_file("wines.txt")

# Відображення вин за спаданням міцності
print("\nВина за спаданням міцності:")
collection.display_wines()

# Відображення загального об’єму вин кожного кольору
print("\nЗагальний об’єм вин кожного кольору:")
collection.total_volume_by_color()
