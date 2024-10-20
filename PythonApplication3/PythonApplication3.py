
import random

inventory = []
monsters_defeated = set()
nights_completed = 0

secret_codes = {
    "FREDDY": "�� �������� ����������� �������, ������� ���������� ���� �������������!",
    "BONNIE": "�� ����� ������ �������: ����������� ��������!",
    "CHICA": "�� �������� �������������� �����!",
}

nights = {
    1: {
        "description": "�� ���������� � �������� ������� Freddy's. ����� ������� ��������, � ������ �������� �����.",
        "puzzle": "��������� ������, ����� ����� �������������.",
        "monsters": ["Freddy", "Bonnie", "Chica"],
        "items": ["�������", "�����", "�������"]
    },
    2: {
        "description": "������ ����. ������������ ���������� �����������.",
        "puzzle": "�������� ���� �� ��������� �������������.",
        "monsters": ["Foxy"],
        "items": ["�����", "�����", "������"]
    },
    3: {
        "description": "������ ����. �� ����������, ��� ���-�� ��������� �� ����.",
        "puzzle": "���������� �������, ����� ��������� ������� ������������.",
        "riddle": "��� ���� �����, �� ������� �� ����������?",
        "answer": "�������"
    }
}


def display_inventory():
    if inventory:
        print("��� ���������:", ", ".join(inventory))
    else:
        print("��� ��������� ����.")


def encounter_monster(monster):
    print(f"�� ����������� � {monster}!")
    if monster == "Freddy":
        print("Freddy �������� �� ���!")
        return True  # ����� ����
    elif monster == "Bonnie" or monster == "Chica":
        print(f"{monster} �������� ��� �������!")
        return random.choice([True, False])  # ��������� ���� ����� ������
    return False  # ����� ��������


def check_secret_code(code):
    if code in secret_codes:
        print(secret_codes[code])
        inventory.append(code)  # ��������� ��������� ������� � ���������
        return True
    return False


def night_one():
    global nights_completed
    print(nights[1]["description"])

    while True:
        action = input("������� ������� (��������� ������, ����� �������, ������ ���): ").lower()

        if action == "��������� ������":
            monster = random.choice(nights[1]["monsters"])
            if encounter_monster(monster):
                print("�� �������! ���� ���������� ������ � ������ ����.")
                return False  # ����� �����

            print(f"�� ������� {monster} �� ������!")
            if monster == "Freddy":
                print("Freddy ������������! ����������� �������!")
                if "�������" in inventory:
                    print("�� �������� Freddy � �� ��������!")
                    monsters_defeated.add(monster)
                    break
                else:
                    print("� ��� ��� ��������!")

        elif action == "����� �������":
            item = random.choice(nights[1]["items"])
            inventory.append(item)
            print(f"�� ����� {item}.")

        elif action.startswith("������ ���"):
            code = action.split()[-1].upper()
            if check_secret_code(code):
                continue  # ��� ������

        display_inventory()

    nights_completed += 1
    return True  # ����� �����


def night_two():
    global nights_completed
    print(nights[2]["description"])

    while True:
        action = input("������� ������� (����������, ����� �������, ������ ���): ").lower()

        if action == "����������":
            if "�����" in inventory:
                print("�� ������������ ����� � ��������� Foxy!")
                monsters_defeated.add("Foxy")
                break
            else:
                print("� ��� ��� ����� ��� ������!")

        elif action == "����� �������":
            item = random.choice(nights[2]["items"])
            inventory.append(item)
            print(f"�� ����� {item}.")
        elif action.startswith("������ ���"):
            code = action.split()[-1].upper()
            if check_secret_code(code):
                continue  # ��� ������

        display_inventory()

    nights_completed += 1
    return True  # ����� �����


def start_game():
    global nights_completed
    while nights_completed < len(nights):
        if nights_completed == 0:
            if not night_one():
                break
        elif nights_completed == 1:
            if not night_two():
                break
        else:
            print("�����������! �� ������ ��� ����!")
            break


# ������ ����
start_game()