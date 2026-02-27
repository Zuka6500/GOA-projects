a = 10 #int
b = 100
c = 1000
d = 2000
e = 3000

f1 = 3.14 #float
f2 = -0.5
f3 = 2.0
f4 = 99.99
f5 = 0.001

s1 = "Hello" #str
s2 = "i"
s3 = "like"
s4 = "python"
s5 = "a lot"

b1 = True #bool
b2 = False
b3 = 5 > 3
b4 = 10 > 0
b5 = "5 >= 4"


#ოპერატორი არის  სპეციალური სიმბოლო ან სიტყვა, რომელიც გამოიყენება მნიშვნელობებზე მოქმედების შესასრულებლად.

#არითმეტიკული ოპერატორი.
a = 5 + 3

#შედარების ოპერატორი.
b = 10 > 3

#ლოგიკური ოპერატორი.
a = True and False

#bool
b1 = True
b2 = False
b3 = 5 > 2
b4 = 10 >= 1
b5 = "a" <= "b"

#შედარების ოპერატორები.
c1 = 5 = 5
c2 = 7 = 3
c3 = 10 > 2
c4 = 4 < 9
c5 = 6 >= 6

#ლოგიკური ოპერატორები.
1 = True and False
2 = True or False
3 = not True
4 = (5 > 3) and (2 < 4)
5 = (10 >= 5) or (3 >= 1)


#Boolean არის მონაცემთა ტიპი პროგრამირებაში, რომელიც ინახავს მხოლოდ ორ შესაძლო მნიშვნელობას.
#1. True – სიმართლე
#2. False - მცდარი


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
result = num1 > num2
print("result")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Is the first number greater than 10:", num1 > 10)
print("Is the second number greater than 20:", num2 > 20)


num = int(input("Enter a number: "))
is_in_range = 100 <= num <= 999
print("Is the number between 100 and ?", is_in_range)