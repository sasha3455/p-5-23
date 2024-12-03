from functools import reduce

# Ваши начальные данные
users = [
    {
        'username': 'john_doe',
        'password': 'password',
        'role': 'user',
        'history': ['Кроссовки Nike', 'Ботинки Timberland'],
        'created_at': '2024-09-01',
    },
    {
        'username': 'admin_user',
        'password': 'admin_password',
        'role': 'admin',
        'history': [],
        'created_at': '2024-01-01',
    },
]

shoes = [
    {'id': 1, 'brand': 'Nike', 'model': 'Air Max', 'size': 42, 'price': 10000, 'rating': 4.5},
    {'id': 2, 'brand': 'Adidas', 'model': 'UltraBoost', 'size': 43, 'price': 12000, 'rating': 4.7},
    {'id': 3, 'brand': 'Puma', 'model': 'Speed', 'size': 40, 'price': 8000, 'rating': 4.3},
    {'id': 4, 'brand': 'Timberland', 'model': 'PRO', 'size': 44, 'price': 15000, 'rating': 4.8},
]

# Функции для пользователей
def user_menu():
    print("Добро пожаловать в магазин обуви!")
    print("Пожалуйста, авторизуйтесь.")
    username = input("Логин: ")
    password = input("Пароль: ")

    user = authenticate_user(username, password)
    if user:
        while True:
            print("\nВыберите действие:")
            print("1. Просмотреть каталог обуви")
            print("2. Найти обувь по параметрам")
            print("3. Сортировать обувь по цене")
            print("4. Просмотреть историю покупок")
            print("5. Обновить профиль")
            print("6. Выйти")

            choice = input("Ваш выбор: ")

            if choice == '1':
                view_shoes()
            elif choice == '2':
                search_shoes()
            elif choice == '3':
                sort_shoes_by_price()
            elif choice == '4':
                view_purchase_history(user)
            elif choice == '5':
                update_profile(user)
            elif choice == '6':
                break
            else:
                print("Неверный выбор! Попробуйте снова.")
    else:
        print("Неверный логин или пароль.")

def view_shoes():
    print("Каталог обуви:")
    # Применяем map для вывода списка с увеличенной ценой
    updated_shoes = list(map(lambda shoe: {**shoe, 'price': shoe['price'] * 1.1}, shoes))  # Увеличиваем цены на 10%
    for shoe in updated_shoes:
        print(f"{shoe['brand']} {shoe['model']} - {shoe['size']} - {shoe['price']} - {shoe['rating']}")

def search_shoes():
    brand = input("Введите бренд для поиска: ")
    size = int(input("Введите размер: "))
    found_shoes = filter(lambda shoe: shoe['brand'] == brand and shoe['size'] == size, shoes)
    print("Результаты поиска:")
    for shoe in found_shoes:
        print(f"{shoe['brand']} {shoe['model']} - {shoe['size']} - {shoe['price']} - {shoe['rating']}")

def sort_shoes_by_price():
    sorted_shoes = sorted(shoes, key=lambda shoe: shoe['price'])
    print("Обувь, отсортированная по цене:")
    for shoe in sorted_shoes:
        print(f"{shoe['brand']} {shoe['model']} - {shoe['price']}")

def view_purchase_history(user):
    print("История ваших покупок:")
    for item in user['history']:
        print(item)

def update_profile(user):
    new_password = input("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно обновлен!")

# Функции для администраторов
def admin_menu():
    print("Добро пожаловать в систему управления магазином обуви!")
    print("Пожалуйста, авторизуйтесь.")
    username = input("Логин: ")
    password = input("Пароль: ")

    admin = authenticate_admin(username, password)
    if admin:
        while True:
            print("\nВыберите действие:")
            print("1. Добавить обувь")
            print("2. Удалить обувь")
            print("3. Редактировать данные о товаре")
            print("4. Управление пользователями")
            print("5. Просмотр статистики")
            print("6. Выйти")

            choice = input("Ваш выбор: ")

            if choice == '1':
                add_shoe()
            elif choice == '2':
                delete_shoe()
            elif choice == '3':
                edit_shoe()
            elif choice == '4':
                manage_users()
            elif choice == '5':
                view_statistics()
            elif choice == '6':
                break
            else:
                print("Неверный выбор! Попробуйте снова.")
    else:
        print("Неверный логин или пароль.")

def add_shoe():
    brand = input("Введите бренд: ")
    model = input("Введите модель: ")
    size = int(input("Введите размер: "))
    price = int(input("Введите цену: "))
    rating = float(input("Введите рейтинг: "))
    new_shoe = {'id': len(shoes) + 1, 'brand': brand, 'model': model, 'size': size, 'price': price, 'rating': rating}
    shoes.append(new_shoe)
    print("Обувь успешно добавлена!")

def delete_shoe():
    shoe_id = int(input("Введите ID обуви для удаления: "))
    shoe_to_delete = next((shoe for shoe in shoes if shoe['id'] == shoe_id), None)
    if shoe_to_delete:
        shoes.remove(shoe_to_delete)
        print("Обувь успешно удалена!")
    else:
        print("Обувь не найдена.")

def edit_shoe():
    shoe_id = int(input("Введите ID обуви для редактирования: "))
    shoe_to_edit = next((shoe for shoe in shoes if shoe['id'] == shoe_id), None)
    if shoe_to_edit:
        new_price = int(input(f"Введите новую цену для {shoe_to_edit['model']}: "))
        new_rating = float(input(f"Введите новый рейтинг для {shoe_to_edit['model']}: "))
        shoe_to_edit['price'] = new_price
        shoe_to_edit['rating'] = new_rating
        print("Данные обуви успешно обновлены!")
    else:
        print("Обувь не найдена.")

def manage_users():
    print("Управление пользователями:")
    for user in users:
        print(f"{user['username']} - {user['role']}")
    action = input("Вы хотите удалить или изменить пользователя? (д/м): ")
    if action == 'д':
        username_to_delete = input("Введите логин пользователя для удаления: ")
        user_to_delete = next((user for user in users if user['username'] == username_to_delete), None)
        if user_to_delete:
            users.remove(user_to_delete)
            print("Пользователь успешно удален!")
        else:
            print("Пользователь не найден.")
    elif action == 'м':
        username_to_edit = input("Введите логин пользователя для изменения: ")
        user_to_edit = next((user for user in users if user['username'] == username_to_edit), None)
        if user_to_edit:
            new_role = input("Введите новую роль (user/admin): ")
            user_to_edit['role'] = new_role
            print("Роль пользователя успешно обновлена!")
        else:
            print("Пользователь не найден.")

def view_statistics():
    # Используем reduce для подсчета общей стоимости
    total_price = reduce(lambda total, shoe: total + shoe['price'], shoes, 0)
    print(f"Общая стоимость всех товаров: {total_price}")

    # Используем reduce для подсчета среднего рейтинга
    total_rating = reduce(lambda total, shoe: total + shoe['rating'], shoes, 0)
    average_rating = total_rating / len(shoes) if shoes else 0
    print(f"Средний рейтинг товаров: {average_rating}")

# Функции для аутентификации
def authenticate_user(username, password):
    return next((user for user in users if
                 user['username'] == username and user['password'] == password and user['role'] == 'user'), None)

def authenticate_admin(username, password):
    return next((user for user in users if
                 user['username'] == username and user['password'] == password and user['role'] == 'admin'), None)

# Основной цикл программы
def main():
    role = input("Введите роль (user/admin): ").strip().lower()

    if role == 'user':
        user_menu()
    elif role == 'admin':
        admin_menu()
    else:
        print("Неверная роль. Попробуйте снова.")

if __name__ == "__main__":
    main()

