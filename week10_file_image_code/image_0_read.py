# Image files contain binary data, and reading them 
# as text will lead to decoding errors. 
# So we use 'rb' instead of 'r'

f = open("rick_and_morty.png", 'rb')
#f = open("rick_and_morty.png", 'r')

lines = f.readlines()
print(lines)
f.close()

# Image files can be opened in this way, 
# but we only read its binary info represented as 
# hexadecimal characters like \xe9\x09


