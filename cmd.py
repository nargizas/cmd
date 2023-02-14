import os

os.chdir("C:/")


def print_current_dir():
    print(f"{os.getcwd()}>", end="")


def show_items_in_cur_dir():
    dir_list = sorted(os.listdir())
    for dir in dir_list:
        print(dir, end="    ")
    print()


while True:
    print_current_dir()
    command = input().strip().split()
    match command:
        case ["quit()"]:
            exit(0)

        case ["ls"]:
            show_items_in_cur_dir()

        case ["cd", ".."] | ["cd.."]:
            os.chdir('../')

        case ["cd", path]:
            try:
                os.chdir(path)
            except:
                print("Системе не удается найти указанный путь.")

        case ["mkdir", *dir_names]:
            for dir in dir_names:
                os.mkdir(dir)

        case ["rmdir", *dir_names]:
            for dir in dir_names:
                try:
                    os.rmdir(dir)
                except:
                    print("Папка не пуста.")

        case ["rename", from_name, to_name]:
            try:
                os.rename(from_name, to_name)
            except:
                print('Не удается найти указанный файл.')

        case ["rename", *rest]:
            print('Ошибка в синтаксисе команды.')

        case ["type", path] | ["more", path]:
            with open(path, encoding="utf-8", errors='ignore') as f:
                print(f.read())

    print()
