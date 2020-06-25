def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        print("Username กับ Password ไม่ถูกต้อง")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    showMenu()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Product Price"))
        vatTotal = price+(price*7/100)
        print(vatTotal)
        print("=======ขอบคุณที่ใช้บริการ==========")
    else:
            print(priceCalculator())
            print("=======ขอบคุณที่ใช้บริการ==========")
    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
login()