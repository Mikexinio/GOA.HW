# 5. შექმენით ცვლადი name და გამოიყენეთ .find() ფუნქცია
name = 'goalorienteacademy'

# 1. 'o'
print(name.find('o'))  # შედეგი: 1 (პირველი 'o'-ს ინდექსი)

# 2. 'a'
print(name.find('a'))  # შედეგი: 4 (პირველი 'a'-ს ინდექსი)

# 3. 'y'
print(name.find('y'))  # შედეგი: 6 (ხოლო, ინდექსი y-ს)

# 4. 'x'
print(name.find('x'))  # შედეგი: -1 (არაა ნაპოვნი, ამიტომ -1)
