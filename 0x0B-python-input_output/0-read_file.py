def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_f = f.read()
    for line in f:
        print(line, end='')