#1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.

#2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

#3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).

#4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

#5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

#6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. (მაგალითად: input: "Hello World". output: "HELLO WORLD".

#1.
X = int(input("enter a number: "))
S = X+5
print(S)

#2.
A = int(input("input a number: "))
B = int(input("input a second number: "))
X = A * B
print(X)

#3.
A = input("enter a word: ")
print(len(A))

#4.
A = input("enter first word: ")
B = input("enter second word: ")
C = input("enter third word: ")
print(len(A))
print(len(B))
print(len(C))

#5.
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "") 
    return s == s[::-1] 

#6.
def to_uppercase(s: str) -> str:
    return s.upper()
