text = "   hello world   "
print(text.strip())



name = input("შეიყვანე სახელი: ")
print(name.strip())




word = input("შეიყვანე სიტყვა: ")

print(word.startswith("A"))




website = input("შეიყვანე ვებსაიტი: ")

print(website.startswith("https"))



file_name = input("შეიყვანე ფაილის სახელი: ")

print(file_name.endswith(".py"))




email = input("შეიყვანე ელფოსტა: ")

print(email.endswith("@gmail.com"))



sentence = "my dog is cute"
print(sentence.replace("dog", "cat"))




text2 = input("შეიყვანე წინადადება: ")

print(text2.replace(" ", "-"))



phone = input("შეიყვანე ნომერი: ")

print(phone.replace("-", ""))





text3 = input("შეიყვანე ტექსტი: ")

clean_text = text3.strip()

print(clean_text.startswith("Hello"))





password = input("შეიყვანე პაროლი: ")

print(password[0].isupper())
print(password.endswith("1"))





sentence2 = input("შეიყვანე წინადადება: ")

sentence2 = sentence2.strip()
sentence2 = sentence2.replace(" ", "_")

if not sentence2.endswith("."):
    sentence2 += "."
print(sentence2)





full_name = input("შეიყვანე სრული სახელი: ")

parts = full_name.split()

for i in parts:
    print(i)

print("სიტყვების რაოდენობა:", len(parts))












sentence3 = input("შეიყვანე წინადადება: ")

words = sentence3.split()

print("ყველაზე გრძელი სიტყვა:", max(words, key=len))
print("ყველაზე მოკლე სიტყვა:", min(words, key=len))








numbers = input("შეიყვანე რიცხვები: ")

numbers_list = numbers.split()

integers = []

for i in numbers_list:
    integers.append(int(i))

print("ჯამი:", sum(integers))
print("ყველაზე დიდი:", max(integers))
print("ყველაზე პატარა:", min(integers))