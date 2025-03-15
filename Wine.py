class Wine:
    def __init__(self, brand: str, description: str, strength: float):
        #Ініціалізація вина з маркою, описом і міцністю
        self.__brand = brand
        self.__description = description
        self.__strength = strength

    # Геттери
    def get_brand(self) -> str:
        return self.__brand

    def get_description(self) -> str:
        return self.__description

    def get_strength(self) -> float:
        return self.__strength

    # Сеттери
    def set_brand(self, brand: str):
        self.__brand = brand

    def set_description(self, description: str):
        self.__description = description

    def __str__(self):
        #Відображення вина у зручному форматі
        return f"{self.__brand} ({self.__description}) - {self.__strength}%"

    def is_type(self, wine_type: str) -> bool:
        #Перевіряє, чи належить вино до певного типу (колір або солодкість).
        return wine_type.lower() in self.__description.lower()

    def __lt__(self, other):
        #Перевантаження оператора < для порівняння вин за міцністю.
        if not isinstance(other, Wine):
            raise TypeError("Можна порівнювати тільки об'єкти класу Wine")
        return self.__strength < other.__strength
    
from wine import Wine

# Створення об'єктів класу Wine
wine1 = Wine("Аліготе", "біле сухе", 10.5)
wine2 = Wine("Каберне", "червоне напівсухе", 12.0)

# Вивід об'єктів
print("Вина:")
print(wine1)
print(wine2)

# Перевірка методу is_type()
print("\nПеревірка типу вина:")
print(f"Чи {wine1.get_brand()} біле? -> {wine1.is_type('біле')}")
print(f"Чи {wine2.get_brand()} сухе? -> {wine2.is_type('сухе')}")

# Порівняння вин за міцністю
print("\nПорівняння вин за міцністю:")
if wine1 < wine2:
    print(f"{wine1.get_brand()} слабше за {wine2.get_brand()}")
else:
    print(f"{wine1.get_brand()} міцніше за {wine2.get_brand()}")
