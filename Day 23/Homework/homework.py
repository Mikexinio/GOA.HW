# 1. სია 4 სტრინგით და მეორე ელემენტის გამოყვანა
strings1 = ["apple", "banana", "cherry", "date"]
print("მეორე ელემენტი:", strings1[1])

# 2. სია 4 სტრინგით და მეორე ინდექსის შეცვლა
strings2 = ["apple", "banana", "cherry", "date"]
strings2[1] = "blueberry"
print("შეცვლილი სია:", strings2)

# 3. სია 5 სტრინგით და slicing (positive indexing)
strings3 = ["apple", "banana", "cherry", "date", "elderberry"]
print("პირველი და მეორე ელემენტი (positive indexing):", strings3[0:2])

# 4. სია 5 სტრინგით და slicing (negative indexing)
strings4 = ["apple", "banana", "cherry", "date", "elderberry"]
print("პირველი და მეორე ელემენტი (negative indexing):", strings4[-5:-3])

# 5. სია 6 სტრინგით და slicing (mixed indexing)
strings5 = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
print("პირველი და მეოთხე ელემენტი (mixed indexing):", [strings5[0], strings5[3]])
