menuList = []
def showBill():
    totalPice = 0
    print("---- Life uNI Shop----")
    for number in range(len(menuList)):
        print(menuList[number])
        totalPice += int(menuList[number][1])
    print("Total",totalPice)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])
showBill()