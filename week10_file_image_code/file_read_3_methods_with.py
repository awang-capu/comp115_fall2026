with open("file_data.txt") as file_ref:
    # print(file_ref.read())
    for line in file_ref:
        print(repr(line))