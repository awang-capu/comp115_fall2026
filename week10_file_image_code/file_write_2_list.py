with open("file_greetings.txt", 'w') as r:

    name_list = ['Camryn', 'Mat', 'Sab', 'Arshdeep', 'Jonathan']
    for name in name_list:
        r.write(f"Hello {name}!\n")
    r.write("This is the greeting from COMP115 class!")
