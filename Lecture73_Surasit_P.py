dataMenu = {"ไข่":50,"ปลา":90,"หมู":100,"ไก่":40}
menuList = []
def showBill():
    totalPice = 0
    print("---- Life uNI Shop----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPice += int(menuList[number][1])
    print("Total",totalPice)
    print("========ขอบคุณครับ===========")
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, dataMenu[menuName]])
showBill()