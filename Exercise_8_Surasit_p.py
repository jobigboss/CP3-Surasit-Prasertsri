User_ID = input("Username")
Password = input("Password")
set1 =500
set2 = 1000
set3 = 350
vat = 7/100
if User_ID == "admin" and Password == "1234":
    print("Wlcome to Life Uno Shop")
    print("1.Set Photobook price 500 THB")
    print("2.Gift  set Duo Max T-shirt price 1,000 THB")
    print("3.Gift set Bottle Water pice 350 THB")
    Userbuy = int(input("What would  you like to have ?(Please key number 1 or 2 or 3,)"))
    if Userbuy ==1:
        print("Please confirm")
        print("Y:","Confirm")
        print("N:","Cancel")
        confirm = input("Please key Y or N")
        if confirm == "Y":
            Set_many = int(input("How many  set do you want ?"))
            price = int(set1*Set_many)
            price_vat = int(set1*Set_many*vat)
            print("Photobook", Set_many, "x500", "---------", Set_many * set1, "THB")
            print("Vat 7%", "---------", int(set1*Set_many*vat), "THB")
            print("Total", "---------", price+price_vat, "THB")
            print("Thank you so much")
        else:
            print("ขอบคุณที่ใช้บริการ Life Uni Shop")
    elif Userbuy ==2:
        print("Please confirm")
        print("Y:", "Confirm")
        print("N:", "Cancel")
        confirm = input("Please key Y or N")
        if confirm == "Y":
            Set_many = int(input("How many  set do you want ?"))
            price = int(set2*Set_many)
            price_vat = int(set2*Set_many*vat)
            print("Gift  set Duo Max T-shirt", Set_many, "x1000", "---------", Set_many * set2, "THB")
            print("Vat 7%", "---------", int(set2*Set_many*vat), "THB")
            print("Total", "---------", price+price_vat, "THB")
            print("Thank you so much")
        else:
            print("ขอบคุณที่ใช้บริการ Life Uni Shop")
    elif Userbuy ==3:
        print("Please confirm")
        print("Y:", "Confirm")
        print("N:", "Cancel")
        confirm = input("Please key Y or N")
        if confirm == "Y":
            Set_many = int(input("How many  set do you want ?"))
            price = int(set3 * Set_many)
            price_vat = int(set3 * Set_many * vat)
            print("Gift set Bottle Water", Set_many, "x1000", "---------", Set_many * set3, "THB")
            print("Vat 7%", "---------", int(set3 * Set_many * vat), "THB")
            print("Total", "---------", price + price_vat, "THB")
            print("Thank you so much")
        else:
            print("ขอบคุณที่ใช้บริการ Life Uni Shop")
else:
    print("ตรวจสอบ Username และ Password")
