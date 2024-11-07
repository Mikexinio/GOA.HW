    #1. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ string-ს, შემდეგ შეაერთეთ ისინი და დაპრინტეთ.

#2. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ 5 ელემენტიან რიცხვების სიას, შემდეგ დაპრინტეთ სიის მე-3 ელემენტისა და მე-4 ელემენტის ჯამი.

#3. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ მანძილს კილომეტრში, შემდეგ გადააქციეთ ის მეტრში და დაპრინტეთ.

#4. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ რიცხვს, შემდეგ დაპრინეთ ამ ორი რიცხვიდან უფრო დიდი.

#5. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ სტრინგს, შემდეგ შეაბრუნეთ ეს სტრინგი და დაპრინტეთ.

#1.
def string (str1, str2):
 result = str1+str2
 print(result)

#2.
 def sum(numbers):
    if len(numbers) >= 4:
        result = numbers[2] + numbers[3]
        print(result)
    else:
        print("The list must contain at least 4 elements.")

#3.
meter = 1000
kilometer = 1
result = kilometer * meter
print(result)

#4.
A = 25
B = 25

if A < B:
   print(B)
else:
   print(A)
   if A == B:
    print("this numbers are the same")

#5.
def reverse(x):
   return x[::-1]
x = str(input('input a word: '))
x = reverse(x)
print(x)