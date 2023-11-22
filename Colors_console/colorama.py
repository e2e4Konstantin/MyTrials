import colorama
from colorama import Cursor

colorama.init()


def print_at(row,):
    print(Cursor.POS(1, 1 + row) + str(text))
    time.sleep(0.05)


def count_lines_in_file(file_num, file_name):
    counter_text = f"{file_name[:20]:<20} "
    with open(file_name, mode="rt", encoding="utf-8") as file:
        for line_num, _ in enumerate(file, start=1):
            counter_text += "□"
            print_at(file_num, counter_text)
        print_at(file_num, f"{counter_text} ({line_num})")


def count_all_files(file_names):
    tasks = [
        count_lines_in_file(file_num, file_name)
        for file_num, file_name in enumerate(file_names, start=1)
    ]


if __name__ == "__main__":
    print(colorama.ansi.clear_screen())
    print(colorama.Fore.RED + 'some red text')
    print(colorama.Back.GREEN + 'and with a green background')
    print(colorama.Style.DIM + 'and in dim text')
    print(colorama.Style.RESET_ALL)
    print('back to normal now')

    count_all_files(sys.argv[1:])
