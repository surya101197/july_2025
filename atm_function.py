balance=25000
def credit():
    global balance
    user=int(input("enter credit: "))
    balance+=user
    return balance
def debit():
    global balance
    user=int(input("enter debit "))
    if user>balance:
        return "insufficient balance"
    balance-=user
    return balance
def check():
    global balance
    return balance
while True:
    print("1.Credit")
    print("2.Debit")
    print("3.Check")
    
    user_1=input("Chose an option ")
    if user_1=="1":
        print("After amount credit your balance is", credit())
    elif user_1=="2":
        print("After amount debit your balance is", debit())
    elif user_1=="3":
        print("Your final balance", check())
        break


