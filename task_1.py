def total_salary(path: str) -> tuple:
    '''Function that calculates the total salary and average salary of employees from the file'''
    data = []
    try:
        with open (path, "r") as file:
            data = file.readlines()
        total = 0
        average = 0
        for line in data:
            line = line.split(",")
            total += float(line[1])
        average = total / len(data)
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено")
        exit()
    except ValueError:
        print("Помилка в даних")
        exit()
    except ZeroDivisionError:
        print("Файл пустий")
        exit()
    except Exception as e:
        print(e)
        exit()

file_path = input("Введіть шлях до файлу: ")
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")