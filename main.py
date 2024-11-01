import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Lütfen Bir Uzunluk Girin:"))

parola = ""
for _ in range(uzunluk):
    parola += random.choice(karakterler)

print(parola)
