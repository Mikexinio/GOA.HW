# 1. შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list3 = [True, False]
list4 = [1.1, 2.2, 3.3, 4.4, 5.5]

print(len(list1))  # შედეგი: 3
print(len(list2))  # შედეგი: 4
print(len(list3))  # შედეგი: 2
print(len(list4))  # შედეგი: 5

# 2. შექმენით 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი
listA = []
listB = []
listC = []

listA.append('apple')
listA.append('banana')

listB.append(10)
listB.append(20)

listC.append(True)
listC.append(False)

print(listA)  # შედეგი: ['apple', 'banana']
print(listB)  # შედეგი: [10, 20]
print(listC)  # შედეგი: [True, False]

# 3. შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები, ხოლო მეორეს მე4ე და მე2ე ადგილას
listX = [0, 1, 2]
listY = ['x', 'y', 'z']

listX.insert(0, 'first')  # 0-დამატება
listX.insert(3, 'last')   # 3-დან (მესამე ადგილას)

listY.insert(2, 'middle')  # 2-დან (მესამე ადგილას)
listY.insert(4, 'end')     # 4-დან (მესამე ადგილას)

print(listX)  # შედეგი: ['first', 0, 1, 'last', 2]
print(listY)  # შედეგი: ['x', 'y', 'middle', 'z', 'end']

# 4. შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით
listZ = ['a', 'b', 'c', 'd', 'e']

removed1 = listZ.pop()  # ბოლო ელემენტის ამოშლა
removed2 = listZ.pop(1)  # მეორე ელემენტის (1-დან) ამოშლა

print(listZ)  # შედეგი: ['a', 'c', 'd']
print(removed1)  # შედეგი: 'e'
print(removed2)  # შედეგი: 'b'

# 5. შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში
var1 = "Hello"
var2 = "World"
var3 = "Python"

print(len(var1))  # შედეგი: 5
print(len(var2))  # შედეგი: 5
print(len(var3))  # შედეგი: 6

# 6. კომენტარების გამოყენებით ახსენით რას აკეთებს თითოეული ფუნქცია
# len() - აბრუნებს სიის ან სტრინგის სიგრძეს.
# append() - ემატება ახალი ელემენტი სიაში ბოლო ადგილზე.
# insert() - დაამატებს ახალი ელემენტი მოცემულ ინდექსზე სიაში.
# pop() - ამოშლის ელემენტს მოცემული ინდექსიდან (თუ ინდექსი არ მითითებულია, ამოშლის უკანასკნელ ელემენტს).
