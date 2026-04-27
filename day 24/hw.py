# mutable არის ტიპები, რომლებიც შეგვიძლია შევცვალოთ შექმნის შემდეგ.
# immutable არის ტიპები, რომლებიც არ შეგვიძლია შევცვალოთ შექმნის შემდეგ.
# len() აბრუნებს ობიექტში ელემენტების რაოდენობას (სიგრძეს).

word = "hello"
print(len(word))


sentence = input("შეიყვანე წინადადება: ")
print(len(sentence))



numbers = [3, -1, 5, -10, 0, 7, -2]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("დადებითი:", positive)
print("უარყოფითი:", negative)



numbers = [10, 3, 25, 7, 20, 8]

count = 0

for num in numbers:
    if num % 5 == 0:
        count += 1

print(count)




numbers = [28, 56, 16, 14, 8, 112, 20]

for num in numbers:
    if num % 4 == 0 and num % 7 == 0:
        print(num)







    items = ["a", "b", "c", "d", "e", "f"]

for i in range(len(items)):
    if i % 2 == 0:
        print(items[i])






    items = ["a", "b", "c", "d", "e", "f"]

for i in range(len(items)):
    if i % 2 == 0:
        print(items[i])


 words = ["hello", "programming", "cat", "python", "banana"]

count = 0

for word in words:
    if len(word) > 5:
        count += 1

print(count)





text = "hello world"

for char in text:
    print(char)






text = "hello world"

for char in text:
    if char != " ":
        print(char)






        words = ["apple", "banana", "kiwi", "watermelon"]

for word in words:
    print(word, "-", len(word))