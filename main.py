import random 

simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Введите длинну пароля: "))
random_password = ""

for i in range(password_length):
    random_password += random.choice(simbols)

print(random_password)