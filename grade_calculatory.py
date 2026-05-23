#user input 
marks = int(input("enter your marks: "))

#condition to check marks for grade
if marks >=80 and marks <=100:
 print("Your marks: ",marks)
 print("your grade is A")
elif marks <=70:
 print("Your marks: ",marks)
 print("your grade is B")
elif marks <=60:
 print("Your marks: ",marks)
 print("your grade is c")
elif marks <=50:
 print("Your marks: ",marks)
 print("your grade is D") 
elif marks >=0:
 print("Your marks: ",marks)
 print("invalid grade F")
else:
 print("enter correct marks")