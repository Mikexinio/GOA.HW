# 1. ფუნქცია, რომელიც აგდებს ორ რიცხვს და ბეჭდავს მათ განაყოფს
def divide_numbers(num1, num2):
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide by zero!")

# 2. ფუნქცია, რომელიც აჩვენებს მისალმების მესიჯს
def greet(name):
    print(f"გამარჯობა, {name}!")

# 3. ფუნქცია, რომელიც აკვირდება რამდენი წლისაა მომხმარებელი
def calculate_age(birth_year):
    current_year = 2024  # მიმდინარე წელი
    age = current_year - birth_year
    print(f"თქვენი ასაკია: {age} წელი")

# 4. ფუნქცია, რომელიც გამრავლებს რიცხვს 5-ზე
def multiply_by_five(number):
    print(f"{number} * 5 = {number * 5}")

# 5. ფუნქცია, რომელიც აჩვენებს მომხმარებლის სახელს და ასაკს
def user_info():
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    name = input("შეიყვანეთ თქვენი სახელი: ")
    print(f"თქვენი სახელი არის {name} და თქვენი ასაკია {age} წელი.")

# მაგალითების გაწვდვა
divide_numbers(10, 2)  # 1. მაგალითად: 10 / 2
greet("ნიკა")  # 2. მისალმება
calculate_age(1990)  # 3. დაბადების წელი
multiply_by_five(4)  # 4. მაგალითი: 4 * 5
user_info()  # 5. მომხმარებლის ინფო
