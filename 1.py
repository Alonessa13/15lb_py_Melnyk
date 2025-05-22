# Створюємо базовий клас Character, який описує будь-якого ігрового персонажа
class Character:
    # Конструктор класу __init__ викликається автоматично при створенні об'єкта
    def __init__(self, name, level, health, attack):
        # Зберігаємо передані значення у властивостях об'єкта
        self.name = name        # Ім'я персонажа
        self.level = level      # Рівень персонажа (впливає на силу)
        self.health = health    # Кількість здоров'я
        self.attack = attack    # Сила атаки

    # Метод для виводу інформації про персонажа
    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

# Створюємо об'єкт класу Character
hero = Character("Козак", 1, 100, 15)

# Викликаємо метод info, щоб вивести інформацію про персонажа
hero.info()
