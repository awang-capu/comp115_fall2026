r = open('file_happ_county.txt', 'w')

mood_alice = "Happy"
mood_sheep = "Soso"
r.write(f"{mood_sheep} Sheep hate Alice!\n")
r.write(f"{mood_alice} Alice likes you!\n")

r.close()