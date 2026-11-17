# Right click file -> copy path: Absolute file path
# "file_data.txt" and "./file_data.txt" are relative file paths

file_r = open("file_data.txt", 'r')

# A line of a file: a string ending with newline character '\n'
for line in file_r:
    print(line)
    #print(repr(line))

file_r.close()