file_ref = open("file_data.txt", 'r')

# st = file_ref.read() # a string
# print(st)
# print(type(st))

first_line = file_ref.readline()
print(first_line) 

l = file_ref.readline()
print(l)

lines = file_ref.readlines()
print(lines)

file_ref.close()







