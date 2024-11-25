#1
print("Hello world")

#2
a = 5
b = 10
print(a + b) 

#3
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  


#4
x = 7
y = 2
print(x / y)

#5
a = 10
b = 20
print(a < b) 

#6
print(5 + 5 == 8 + 2)  

#7
x = 5
y = 10
print(x > 3 and y < 15)  

print(x > 3 or y > 15)  

print(not(x > 3))

#8
x = 10
y = 5
z = 20

print(x > y and y < z)  
print(x == 10 or y == 10)  
print(not(x == 5))  
print(x > y and not(z < 15)) 
print(x < 20 or y > 10)  

#9
for i in range(1, 11):
    print(i)

#10
for char in "Hello, World!":
    print(char)

#11
i = 1
while i <= 10:
    print(i)
    i += 1

#12
total = 0
i = 1
while total < 50:
    total += i
    i += 1
print(total)  

#13
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 3, 4, 5, 2])) 

#14
def square_numbers(numbers):
    squares = [5]
    for num in numbers:
        squares.append(num ** 2)
    return squares

print(square_numbers([3, 12, 5, 2, 6])) 

#15
lst = [3, 1, 4, 1, 5]
lst.append(9) 
lst.remove(1)  
lst.sort()  
print(lst)  

text = "hello world"
print(text.upper()) 
print(text.replace("world", "everyone"))  
print(text.split())  
