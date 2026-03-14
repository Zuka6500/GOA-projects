#Sequencing ნიშნავს, რომ ბრძანებები პროგრამაში სრულდება მიმდევრობით, ერთის შემდეგ მეორე.
#Selection ნიშნავს არჩევას, ანუ პროგრამა წყვეტს რა გააკეთოს პირობის მიხედვით.
#ინდენტაცია ნიშნავს კოდის წინ დატოვებულ დაშორებას. ინდენტაცია გამოიყენება მაშინ, როცა იწყება კოდის დასაწყისი.


math_score = float(input("შეიყვანეთ თქვენი მათემატიკის ქულა: "))
english_score = float(input("შეიყვანეთ თქვენი ინგლისურის ქულა: "))
physics_score = float(input("შეიყვანეთ თქვენი ფიზიკის ქულა: "))

if math_score >= 90 and english_score >= 90 and physics_score >= 90:
    print("შესანიშნავი მოსწავლე ხარ!") and print("ყველა საგანში მაღალი შედეგი გაქვს")
elif math_score >= 70 and english_score >= 70 and physics_score >= 70:
        print("კარგი შედეგებია") and print("სასწავლო წელი წარმატებულია")
elif math_score < 50 or english_score < 50 or physics_score < 50:
        print("ერთ-ერთ საგანში დაბალი ქულა გაქვს") and print("მეტი სწავლა დაგჭირდება")
else:
    print("შედეგები საშუალოა") and print("შეგიძლია უკეთესიც")