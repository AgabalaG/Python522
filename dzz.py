import os

file = ".venv/text3.txt"
f = open(file, "w")
f.write("Замена строки в текстовом файле;\n"
        "изменить строку в списке;\n"
        "записать список в файл;\n")

f.close()

if os.path.exists(file):
    f = open(file, "r")
    read_line = f.readlines()
    f.close()

    pos1 = int(input("pos1 = ")) - 1  
    pos2 = int(input("pos2 = ")) - 1

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    if 0 < pos1 <= len(read_line) and 0 < pos2 <= len(read_line):
        if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
            read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
        else:
            print("Такой строки нет")
        print(read_line)
