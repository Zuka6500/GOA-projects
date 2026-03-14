weight = float(input("შეიყვანე წონა კილოგრამებში: "))
height = float(input("შეიყვანე სიმაღლე მეტრებში: "))
age = int(input("შეიყვანე ასაკი: "))
bmi = weight / (height * height)

if bmi < 18.5 and age >= 18:
    print("შენი BMI დაბალია")
    print("შესაძლოა წონის მომატება დაგჭირდეს")
elif bmi >= 18.5 and bmi <= 24.9 and age >= 18:
    print("შენი BMI ნორმალურია")
    print("ჯანმრთელ ფორმაში ხარ")
elif bmi >= 25 and bmi < 30 or age < 18:
    print("BMI საშუალოზე მაღალია")
    print("ჯანსაღი კვება მნიშვნელოვანია")
elif bmi >= 30:
    print("BMI მაღალია")
    print("სასურველია ექიმთან კონსულტაცია")
else:
    print("მონაცემები ვერ დამუშავდა")
    print("სცადე თავიდან")