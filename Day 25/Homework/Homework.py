my_string = "Hello"
second_character = my_string[1]
print("მეორე ასო:", second_character)

a = 5
b = 10
sum_result = a + b
print("ჯამი:", sum_result)

string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print("შეერთებული ვერსია:", concatenated_string)

x = 7
y = 2
division_result = x / y
print("განაყოფი:", division_result)

is_greater = (5 > 3)
print("5 დიდია 3-ზე:", is_greater)

comparison_result = (5 + 5 == 8 + 2)
print("5 + 5 == 8 + 2:", comparison_result)

print(5 > 3 and 2 < 4)
print(5 < 3 or 2 < 4)
print(not(5 > 3))
print(5 == 5 and 1 != 1)
print(4 <= 4 or 10 > 5)

print("1-დან 10-მდე რიცხვები:")
for i in range(1, 11):
    print(i)

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print("რიცხვების ჯამი:", sum_of_numbers)

for char in "Hello, World!":
    print(char)

print("1-დან 10-მდე რიცხვები (while):")
i = 1
while i <= 10:
    print(i)
    i += 1

print("1-დან 100-მდე რიცხვები (50-60 გამოტოვებით):")
i = 1
while i <= 100:
    if 50 <= i < 60:
        i += 1
        continue
    print(i)
    i += 1

print("რიცხვების შეკრება, სანამ ჯამი 50-ს არ გაუტოლდება:")
total_sum = 0
i = 1
while total_sum < 50:
    total_sum += i
    i += 1
print("ჯამი:", total_sum)
