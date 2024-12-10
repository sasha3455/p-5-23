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
    try:
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
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def admin_menu():
    print("Добро пожаловать, администратор!")
    try:
        while True:
            print("\nВыберите действие:")
            print("1. Добавить товар")
            print("2. Удалить товар")
            print("3. Просмотреть статистику")
            print("4. Управление пользователями")
            print("5. Выйти")

            choice = input("Ваш выбор: ")

            if choice == '1':
                add_shoe()
            elif choice == '2':
                delete_shoe()
            elif choice == '3':
                view_statistics()
            elif choice == '4':
                manage_users()
            elif choice == '5':
                break
            else:
                print("Неверный выбор! Попробуйте снова.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def view_shoes():
    try:
        print("Каталог обуви:")
        for shoe in shoes:
            print(f"{shoe['brand']} {shoe['model']} - {shoe['size']} - {shoe['price']} - {shoe['rating']}")
    except Exception as e:
        print(f"Ошибка при просмотре каталога: {e}")

def search_shoes():
    try:
        brand = input("Введите бренд для поиска: ")
        size = int(input("Введите размер: "))
        found_shoes = filter(lambda shoe: shoe['brand'] == brand and shoe['size'] == size, shoes)
        print("Результаты поиска:")
        found = False
        for shoe in found_shoes:
            print(f"{shoe['brand']} {shoe['model']} - {shoe['size']} - {shoe['price']} - {shoe['rating']}")
            found = True
        if not found:
            print("Обувь не найдена.")
    except ValueError:
        print("Ошибка: размер должен быть числом.")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")

def sort_shoes_by_price():
    try:
        sorted_shoes = sorted(shoes, key=lambda shoe: shoe['price'])
        print("Обувь, отсортированная по цене:")
        for shoe in sorted_shoes:
            print(f"{shoe['brand']} {shoe['model']} - {shoe['price']}")
    except Exception as e:
        print(f"Ошибка при сортировке: {e}")

def view_purchase_history(user):
    try:
        print("История ваших покупок:")
        if user['history']:
            for item in user['history']:
                print(item)
        else:
            print("История покупок пуста.")
    except Exception as e:
        print(f"Ошибка при просмотре истории: {e}")

def update_profile(user):
    try:
        new_password = input("Введите новый пароль: ")
        user['password'] = new_password
        print("Пароль успешно обновлен!")
    except Exception as e:
        print(f"Ошибка при обновлении профиля: {e}")

# Функции для администраторов
def add_shoe():
    try:
        brand = input("Введите бренд: ")
        model = input("Введите модель: ")
        size = int(input("Введите размер: "))
        price = float(input("Введите цену: "))
        rating = float(input("Введите рейтинг: "))
        new_shoe = {
            'id': len(shoes) + 1,
            'brand': brand,
            'model': model,
            'size': size,
            'price': price,
            'rating': rating,
        }
        shoes.append(new_shoe)
        print("Товар успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении товара: {e}")

def delete_shoe():
    try:
        shoe_id = int(input("Введите ID товара для удаления: "))
        shoes[:] = [shoe for shoe in shoes if shoe['id'] != shoe_id]
        print("Товар успешно удален!")
    except Exception as e:
        print(f"Ошибка при удалении товара: {e}")

def manage_users():
    try:
        print("Выберите действие:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Редактировать пользователя")
        choice = input("Ваш выбор: ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (user/admin): ").strip().lower()
            new_user = {
                'username': username,
                'password': password,
                'role': role,
                'history': [],
                'created_at': '2024-12-10'
            }
            users.append(new_user)
            print("Пользователь успешно добавлен!")
        elif choice == '2':
            username = input("Введите имя пользователя для удаления: ")
            users[:] = [user for user in users if user['username'] != username]
            print("Пользователь успешно удален!")
        elif choice == '3':
            username = input("Введите имя пользователя для редактирования: ")
            user = next((user for user in users if user['username'] == username), None)
            if user:
                user['password'] = input(f"Введите новый пароль ({user['password']}): ") or user['password']
                user['role'] = input(f"Введите новую роль ({user['role']}): ").strip().lower() or user['role']
                print("Пользователь успешно обновлен!")
            else:
                print("Пользователь не найден.")
        else:
            print("Неверный выбор!")
    except Exception as e:
        print(f"Ошибка при управлении пользователями: {e}")

# Функции для аутентификации
def authenticate_user(username, password):
    try:
        return next((user for user in users if user['username'] == username and user['password'] == password and user['role'] == 'user'), None)
    except Exception as e:
        print(f"Ошибка аутентификации: {e}")
        return None

def authenticate_admin(username, password):
    try:
        return next((user for user in users if user['username'] == username and user['password'] == password and user['role'] == 'admin'), None)
    except Exception as e:
        print(f"Ошибка аутентификации: {e}")
        return None

# Основной цикл программы
def main():
    try:
        role = input("Введите роль (user/admin): ").strip().lower()
        if role == 'user':
            user_menu()
        elif role == 'admin':
            admin_menu()
        else:
            print("Неверная роль. Попробуйте снова.")
    except Exception as e:
        print(f"Ошибка в главном меню: {e}")

if __name__ == "__main__":
    main()

