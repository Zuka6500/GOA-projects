# 1
name = "Zuka"
print(name[0])

# 2
surname = "Katsarava"
print(surname[-1])

# 3
word = "Python"
print(word[2])

# 4
word1 = "Programming"
print(word1[:4])

# 5
word2 = "Computer"
print(word2[-3:])

# 6
word3 = "HelloWorld"
print(word3[3:7])

# 7
word4 = "Georgia"
print(word4[2:6])

# 8
favorite_word = "Apple"

if favorite_word[0] == "A":
    print(favorite_word[:3])
else:
    print(favorite_word[-3:])

# 9
word5 = "Education"
print(word5[1:-1])

# 10
word6 = "Developer"
new_word = word6[:3] + word6[-3:]
print(new_word)

# 11
sentence = "Python is very interesting"
space_index = sentence.index(" ")
print(sentence[:space_index])

# 12
word7 = "abcdef"
print(word7[::2])

# 13
my_list = [10, "hello", 3.14, True, "Python", 50, "car", False]
print(my_list[2:6])

# 14
musicians = ["Eminem", "Tupac", "Weeknd", "Travis Scott", "Kanye West", "Future"]
print(musicians[-2:])