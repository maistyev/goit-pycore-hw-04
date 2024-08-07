def get_cats_info(path: str):
    '''Function that reads the file and returns a list of dictionaries with information about cats'''
    data = []
    try:
        with open(path, "r") as file:
            data = file.readlines()
        cats = []
        for line in data:
            line = line.split(",")
            cats.append({"id": line[0], "name": line[1], "age": int(line[2])}) # Add a dictionary with information about the cat to the list
        return cats
    except FileNotFoundError:
        print("Файл не знайдено")
        exit()
    except ValueError:
        print("Помилка в даних")
        exit()
    except Exception as e:
        print(e)
        exit()

file_path = input("Введіть шлях до файлу: ")
cats = get_cats_info(file_path)
print(cats)
