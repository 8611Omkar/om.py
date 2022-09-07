def add(num1,num2):
    result = num1 + num2
    print(num1 ,"+", num2, "=", result)
    
def sub(num1,num2):
    result = num1 - num2
    print(num1 ,"-", num2, "=", result)
    
def multi(num1,num2):
    result = num1 * num2
    print(num1 ,"*", num2, "=", result)
    
def division(num1,num2):
    result = num1 / num2
    print(num1 ,"/", num2, "=", result)
    
def percentage(num1,num2):
    result = num1 % num2
    print(num1 ,"%", num2, "=", result)
    
choice=input("Enter operator: +, -, *, /, % = ")    
firstnum1 = float(input("Enter a number :"))
secondnum2 = float(input("Enter a number :"))
# print(num1 ,"%",  num2, "=" )
if choice =="+":
    add(firstnum1,secondnum2)
if choice =="-":
    sub(firstnum1,secondnum2)
if choice =="*":
    multi(firstnum1,secondnum2)
if choice =="/":
    division(firstnum1,secondnum2)
if choice =="%":
    percentage(firstnum1,secondnum2)


 