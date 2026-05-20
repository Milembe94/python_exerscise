total = 0
choice =0
print("CALCULATOR")

while choice !=5:
    print("1. Addition\n2.Substraction\n3.Multiplication\n4.Divission\n5.Exite")
    choice = int(input("Enter chice: "))
    
    match choice:
        case 1:
            print("You choose addition")
            number1=int(input("Enter first number: "))
            number2=int(input("Enter second number: "))
            total = number1 + number2
            print( "The total: ", total )
        case 2:
            print("You choose substraction")
            number1=int(input("Enter first number: "))
            number2=int(input("Enter second number: "))
            total = number1 - number2
            print("The total: ", total)
        case 3:
            print("You choose multiplication")
            number1=int(input("Enter first number: "))
            number2=int(input("Enter second number: "))
            total = number1 * number2
            print("The total: ", total )
        case 4:
            print("You choose divission")
            number1=int(input("Enter first number: "))
            number2=int(input("Enter second number: "))
            total = number1 / number2
            if number1 == 0 or number2 ==0:
                print("There is no number divided by 0")
            else:
                print("The total: ", total )
        case 5:
            print("EXITE")
        case _:
             print("invalid choice")
