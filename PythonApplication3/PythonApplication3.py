
import random

inventory = []
monsters_defeated = set()
nights_completed = 0

secret_codes = {
    "FREDDY": "Вы получили специальный фонарик, который отпугивает всех аниматроников!",
    "BONNIE": "Вы нашли редкий предмет: музыкальную шкатулку!",
    "CHICA": "Вы получили дополнительную жизнь!",
}

nights = {
    1: {
        "description": "Вы находитесь в охранной комнате Freddy's. Стены покрыты граффити, и слышны странные звуки.",
        "puzzle": "Проверьте камеры, чтобы найти аниматроников.",
        "monsters": ["Freddy", "Bonnie", "Chica"],
        "items": ["фонарик", "замок", "записка"]
    },
    2: {
        "description": "Вторая ночь. Аниматроники становятся агрессивнее.",
        "puzzle": "Защитите себя от нападения аниматроников.",
        "monsters": ["Foxy"],
        "items": ["спрей", "дверь", "запись"]
    },
    3: {
        "description": "Третья ночь. Вы чувствуете, что кто-то наблюдает за вами.",
        "puzzle": "Разгадайте загадку, чтобы отключить систему безопасности.",
        "riddle": "Что идет вверх, но никогда не опускается?",
        "answer": "возраст",
        "monsters": ["Freddy", "Chica"],
        "items": ["ключ", "фонарик", "диск"]
    }
}


def display_inventory():
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")


def encounter_monster(monster):
    print(f"Вы столкнулись с {monster}!")
    if monster == "Freddy":
        print("Freddy нападает на вас!")
        return True  # Игрок убит
    elif monster == "Bonnie" or monster == "Chica":
        print(f"{monster} пытается вас поймать!")
        return random.choice([True, False])  # Случайный шанс убить игрока
    return False  # Игрок выживает


def check_secret_code(code):
    if code in secret_codes:
        print(secret_codes[code])
        inventory.append(code)  # Добавляем секретный предмет в инвентарь
        return True
    return False


def night_one():
    global nights_completed
    print(nights[1]["description"])

    while True:
        action = input("Введите команду (проверить камеры, взять предмет, ввести код): ").lower()

        if action == "проверить камеры":
            monster = random.choice(nights[1]["monsters"])
            if encounter_monster(monster):
                print("Вы погибли! Игра начинается заново с первой ночи.")
                return False  # Игрок погиб

            print(f"Вы увидели {monster} на камере!")
            if monster == "Freddy":
                print("Freddy приближается! Используйте фонарик!")
                if "фонарик" in inventory:
                    print("Вы ослепили Freddy и он отступил!")
                    monsters_defeated.add(monster)
                    break
                else:
                    print("У вас нет фонарика!")

        elif action == "взять предмет":
            item = random.choice(nights[1]["items"])
            inventory.append(item)
            print(f"Вы взяли {item}.")
        elif action.startswith("ввести код"):
            code = action.split()[-1].upper()
            if check_secret_code(code):
                continue  # Код принят

        display_inventory()

    nights_completed += 1
    return True  # Игрок выжил


def night_two():
    global nights_completed
    print(nights[2]["description"])

    while True:
        action = input("Введите команду (защититься, взять предмет, ввести код): ").lower()

        if action == "защититься":
            if "спрей" in inventory:
                print("Вы использовали спрей и отпугнули Foxy!")
                monsters_defeated.add("Foxy")
                break
            else:
                print("У вас нет спрея для защиты!")

        elif action == "взять предмет":
            item = random.choice(nights[2]["items"])
            inventory.append(item)
            print(f"Вы взяли {item}.")

        elif action.startswith("ввести код"):
            code = action.split()[-1].upper()
            if check_secret_code(code):
                continue  # Код принят

        display_inventory()
    nights_completed += 1
    return True  # Игрок выжил


def night_three():
    global nights_completed
    print(nights[3]["description"])

    while True:
        action = input("Введите команду (разгадать загадку, взять предмет, ввести код): ").lower()

        if action == "разгадать загадку":
            print(nights[3]["riddle"])
            answer = input("Ваш ответ: ").lower()
            if answer == nights[3]["answer"]:
                print("Загадка разгадана, система безопасности отключена!")
                break
            else:
                print("Неправильно. Попробуйте еще раз.")

        elif action == "взять предмет":
            item = random.choice(nights[3]["items"])
            inventory.append(item)
            print(f"Вы взяли {item}.")

        elif action.startswith("ввести код"):
            code = action.split()[-1].upper()
            if check_secret_code(code):
                continue  # Код принят

        display_inventory()

        if random.random() < 0.3:
            monster = random.choice(nights[3]["monsters"])
            if encounter_monster(monster):
                print("Вы погибли! Игра начинается заново с первой ночи.")
                return False  # Игрок погиб

    nights_completed += 1
    return True  # Игрок выжил


def start_game():
    print("Добро пожаловать в игру 'Five Nights at Freddy's'!")
    
    if night_one():
        if night_two():
            if night_three():
                print("Поздравляем! Вы прошли все три ночи и выжили!")
