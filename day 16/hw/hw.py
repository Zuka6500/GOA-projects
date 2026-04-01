i = 0

while i <= 100:
    print(i)
    i += 1

i = 40

while i <= 250:
    print(i)
    i += 2

i = 200

while i <= 400:

    if i % 4 == 0 and i % 5 == 0:
        print(i)
    i += 1

num = int(input("შეიყვანე რიცხვი: "))

i = 2
while i <= num:
    print(i)
    i += 1

num = int(input("შეიყვანე რიცხვი: "))

while num >= 0:
    print(num)
    num -= 1

number = 7
guess = int(input("გამოიცანი რიცხვი: "))

while guess != number:
    guess = int(input("არასწორია, სცადე თავიდან: "))

print("გილოცავ, სწორად გამოიცანი")