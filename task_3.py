import os
import sys
from colorama import Fore, Style

def visualize_directory(path, prefix=""):
    """
    Рекурсивно візуалізує структуру директорії.
    """
    if not os.path.exists(path):
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.")
        return
    
    if not os.path.isdir(path):
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.")
        return

    # Отримуємо список всіх елементів в директорії
    items = os.listdir(path)
    
    # Сортуємо елементи: спочатку директорії, потім файли
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x))

    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        
        # Визначаємо, чи це останній елемент
        is_last = index == len(items) - 1
        
        # Вибираємо відповідний символ для з'єднання
        if is_last:
            connector = "└── "
        else:
            connector = "├── "

        if os.path.isdir(item_path):
            # Виводимо ім'я директорії синім кольором
            print(f"{prefix}{connector}{Fore.BLUE}{item}{Style.RESET_ALL}")
            
            # Рекурсивно візуалізуємо вміст піддиректорії
            if is_last:
                visualize_directory(item_path, prefix + "    ")
            else:
                visualize_directory(item_path, prefix + "│   ")
        else:
            # Виводимо ім'я файлу зеленим кольором
            print(f"{prefix}{connector}{Fore.GREEN}{item}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Будь ласка, вкажіть шлях до директорії як аргумент.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
        sys.exit(1)

    directory_path = sys.argv[1]
    print(f"Візуалізація структури директорії: {directory_path}\n")
    visualize_directory(directory_path)