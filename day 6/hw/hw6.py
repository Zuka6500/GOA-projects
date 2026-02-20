#მონაცემთა ტიპები საჭიროა იმისთვის, რომ: კომპიუტერმა იცოდეს როგორ შეინახოს მონაცემი მეხსიერებაში.

#input მაგალითები არის კლავიატურა, ჯოისტიკი, მაუსი და ა.შ.
#output მაგალითები არის მონიტორი, პრინტერი, დინამიკი და ა.შ.

name = "Zuka"   # string
age = 15   # integer
height = 1.78   # float

print(type(name))
print(type(age))
print(type(height))


km = float(input("შეიყვანეთ მანძილი კილომეტრებში: "))
meters = km * 1000
print("მანძილი მეტრებში არის:", meters)


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print("რიცხვების ჯამი არის:", num1 + num2)
print( "რიცხვების სხვაობა არის:", num1 - num2)
print("რიცხვების ნამრავლი არის:", num1 * num2)
print("რიცხვების განაყოფი არის:", num1 / num2)



#BMI კალკულატორი
weight = float(input("შეიყვანეთ თქვენი წონა კილოგრამებში: "))
height = float(input("შეიყვანეთ თქვენი სიმაღლე მეტრებში: "))

bmi = weight / (height * height)

print("თქვენი BMI არის:", bmi)