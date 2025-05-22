# Базовий клас Character
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"{self.name}: Рівень {self.level}, Здоров'я {self.health}, Атака {self.attack}")

    def attack_enemy(self, enemy):
        print(f"{self.name} атакує {enemy.name} на {self.attack} шкоди!")
        enemy.health -= self.attack
        if enemy.health < 0:
            enemy.health = 0

    # Загальний метод відновлення здоров'я
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} відновлює {amount} здоров'я! Поточне здоров'я: {self.health}")

# Підклас Warrior (воїн), наслідує базовий Character
class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)  # Викликаємо конструктор базового класу
        self.armor = armor  # Додаємо унікальну властивість - броня

# Підклас Mage (маг)
class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana  # Унікальна властивість - мана для магічних атак

# Підклас Archer (лучник)
class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows  # Унікальна властивість - кількість стріл

# Створюємо по одному об'єкту кожного класу
w = Warrior("Герой-воїн", 3, 150, 25, armor=30)
m = Mage("Чарівник", 2, 100, 20, mana=50)
a = Archer("Стрілець", 2, 110, 18, arrows=10)

# Виводимо інформацію
w.info()
m.info()
a.info()

# Відновлюємо здоров'я мага
m.heal(20)
