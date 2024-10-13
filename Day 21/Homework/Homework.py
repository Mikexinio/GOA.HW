# 1. სიაში შეინახეთ 5 რიცხვი და პირველი და მეოთხე ელემენტების ნამრავლი
numbers = [3, 5, 7, 2, 9]
result = numbers[0] * numbers[3]
print("პირველი და მეოთხე ელემენტების ნამრავლი:", result)

# 2. სიაში შეინახეთ 7 სტრინგი და შუა სტრინგის პოვნა
strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
middle_index = len(strings) // 2
print("შუა სტრინგი:", strings[middle_index])

# 3. ცვლადში შეინახეთ სტრინგი და მეორე ასოს დაპრინტვა
my_string = "Hello"
print("სტრინგის მეორე ასო:", my_string[1])  # ინდექსი იწყება 0-დან

# 4. ვენდინგ მანქანის თამაში
products = ["კოკა-კოლა", "ნატურალური сокი", "წყალი", "ბრაუნი", "ჩიპსი"]

print("\nდაგვირგვინებული ვენდინგ მანქანა")
print("მშვენიერი პროდუქტების სია:")
for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")

# მომხმარებლის არჩევანი
choice = int(input("შეიყვანეთ პროდუქტის ნომერი: ")) - 1

# პროდუქტის დაპრინტვა
if 0 <= choice < len(products):
    print(f"თქვენი არჩევანი: {products[choice]}")
else:
    print("არასწორი ნომერი, გთხოვთ, სცადეთ ისევ.")
