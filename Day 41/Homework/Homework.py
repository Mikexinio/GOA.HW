def vending_machine(products, prices, user_balance):
    print("მიუწვდომელი პროდუქტები:")
    
    for idx, product in enumerate(products):
        print(f"{idx}. {product} - {prices[idx]} ლარი")
    
    choice = int(input("\nაირჩიეთ პროდუქტის ინდექსი: "))
    
    if user_balance >= prices[choice]:
        user_balance -= prices[choice]
        print(f"\nგილოცავთ! თქვენ შეიძინეთ {products[choice]}. დარჩენილი ფული: {user_balance} ლარი.")
    else:
        print(f"\nსამწუხაროდ, არ გაქვთ საკმარისი ფული {products[choice]}-ის შეძენისთვის. დარჩენილი ფული: {user_balance} ლარი.")

products = ["კოკა-კოლა", "ბატონი", "ჩიპსი", "წყალი"]
prices = [2.50, 1.00, 1.50, 0.80]
user_balance = 2.00

vending_machine(products, prices, user_balance)