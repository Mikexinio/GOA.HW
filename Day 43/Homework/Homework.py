#1.
numbers = [5, 10, 15, 20, 25]
total_sum = sum(numbers)
print("რიცხვების ჯამი:", total_sum)

#2.
numbers = [5, 10, 15, 20, 25]
max_value = max(numbers)
print("უდიდესი რიცხვი:", max_value)

#3.
numbers = [5, 10, 15, 20, 25]
min_value = min(numbers)
print("უმცირესი რიცხვი:", min_value)

#4.
numbers = [5, 10, 15, 20, 25]
length = len(numbers)
print("სიის სიგრძე:", length)

#5.
words = ["apple", "banana", "cherry", "date", "elderberry"]
words.append("fig")
print("განახლებული სია:", words)

#6.
words = ["apple", "banana", "cherry", "date", "elderberry"]
words.insert(2, "blueberry")  # აქ 2 არის ინდექსი, სადაც სიტყვა "blueberry" დაემატება
print("განახლებული სია:", words)

#7.
words = ["apple", "banana", "cherry", "date", "elderberry"]
removed_word = words.pop(1)  # ამოაგდებს ინდექსზე 1 (banana)
print("ამოღებული სიტყვა:", removed_word)
print("განახლებული სია:", words)