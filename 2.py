# Використовуємо той самий клас Character, але додаємо новий метод для бою
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"{self.name}: Рівень {self.level}, Здоров'я {self.health}, Атака {self.attack}")

    # Метод для атаки іншого персонажа
    def attack_enemy(self, enemy):
        print(f"{self.name} атакує {enemy.name} на {self.attack} шкоди!")
        # Зменшуємо здоров'я суперника на величину атаки
        enemy.health -= self.attack

        # Якщо здоров'я стало менше 0, встановлюємо 0
        if enemy.health < 0:
            enemy.health = 0

# Створюємо двох персонажів для симуляції бою
hero1 = Character("Лицар", 2, 120, 20)
hero2 = Character("Бандит", 1, 90, 15)

# Виводимо початкову інформацію
hero1.info()
hero2.info()

# Перший персонаж атакує другого
hero1.attack_enemy(hero2)

# Виводимо інформацію після атаки
hero2.info()
