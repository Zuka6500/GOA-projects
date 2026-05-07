numbers = [1, 2, 3]
numbers.append(4)

print(numbers)





numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)

print(numbers)




words = ["apple", "banana", "orange"]

words.remove("banana")

print(words)



my_list = [10, 20, 30]

my_list.remove(20)  # შლის 20-ს
my_list.pop(1)      # შლის ინდექს 1-ზე მდგომს



numbers = [5, 10, 15, 20]

removed = numbers.pop()

print("ამოღებული:", removed)
print("განახლებული სია:", numbers)




numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)




numbers = [8, 3, 1, 7, 2]

numbers.sort()

print(numbers)




numbers = [1, 2, 3]

numbers.reverse()

print(numbers)




words = ["cat", "dog", "bird"]

words.reverse()

print(words)



numbers = [1, 2, 3]

numbers.clear()

print(numbers)



numbers = [10, 20, 30, 40]

index_num = numbers.index(30)

print(index_num)

