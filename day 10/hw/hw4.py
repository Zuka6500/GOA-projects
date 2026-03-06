username = input("შეიყვანე მომხმარებლის სახელი: ")
password = input("შეიყვანე პაროლი: ")

if username == "admin" and password == "superSecretPassword":
    print("მოგესალმები, ადმინ!")
elif username == "guest" and password == "1234":
    print("მოგესალმები, სტუმარო!")
else:
    print("მომხმარებელი არ მოიძებნა!")