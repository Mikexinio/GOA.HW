# მომხმარებლის ასაკის და მამამისის ასაკის მიღება
user_age = int(input("შეიყვანეთ თქვენი ასაკი: "))
father_age = int(input("შეიყვანეთ მამამისის ასაკი: "))

# 23 წლის შემდეგ
future_user_age = user_age + 23
future_father_age = father_age + 23

# რამდენჯერ იქნება მამამისი უფრო ძველი
age_ratio = future_father_age / future_user_age

# შედეგის გამოტანა
print(f"23 წლის შემდეგ, მამა {age_ratio:.2f} ჯერ უფრო ძველი იქნება თქვენზე.")
