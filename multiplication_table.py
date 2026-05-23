#input section

number=int(input("Enter number: "))
print("MULTIPLICATION TABLE OF ",number)
#loop execution section
for i in range( number):
    print(number, "x", i ,"=", number * i)
