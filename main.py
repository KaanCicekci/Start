import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Lütfen Bir Uzunluk Girin:"))
b = random.choice(karakterler)
parola = "".join(random.sample(karakterler,uzunluk))
print("işte yeni parolan " + parola)
