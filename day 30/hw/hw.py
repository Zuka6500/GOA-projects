# lower მეთოდი ყველა დიდ ასოს პატარა ასოდ გადააქცევს

text = "HELLO WORLD"
print(text.lower())

word = "PYTHON"
print(word.lower())

# upper მეთოდი ყველა პატარა ასოს დიდ ასოდ გადააქცევს
text = "hello world"
print(text.upper())

word = "python"
print(word.upper())



user_word = input("შეიყვანე სიტყვა: ")
print(user_word.upper())



# title მეთოდი ყოველი სიტყვის პირველ ასოს დიდად გადააქცევს
sentence = "hello world"
print(sentence.title())



my_list = ["hello world", "python programming", "good morning"]

for i in my_list:
    print(i.title())



    mixed = "PyThOn"
print(mixed.swapcase())



text3 = "banana"
print(text3.count("a"))




sentence2 = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")

print(sentence2.count(symbol))




name = input("შეიყვანე სახელი: ")
surname = input("შეიყვანე გვარი: ")

print(name.title(), surname.title())






text4 = input("შეიყვანე წინადადება: ")

vowels = "აეიოუAEIOUaeiou"
count = 0

for letter in text4:
    if letter in vowels:
        count += 1

print("ხმოვნების რაოდენობა:", count)

