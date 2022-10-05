import os
from art import logo
print(logo)

calculation_on = True
count = 0

def add(n1,n2):
    return n1 + n2
    
def sub(n1,n2):
    return n1 - n2
    
def mul(n1,n2):
    return n1*n2
    
def divi(n1,n2):
    return n1/n2
    

while(calculation_on == True):
    
    if count == 0:
    
        n1 = float(input("what is the first number ? : "))
        operation = input("+\n-\n*\n/\nPick an operation. ")
        n2 = float(input("what is the next number ? : "))
    else:
        
        n1 = n3
        operation = input("+\n-\n*\n/\nPick an operation. ")
        n2 = float(input("what is the next number ? : "))
   
    
    if operation == "+":
        n3 = add(n1,n2)
        print(f" {n1} + {n2} = {n3}")
    elif operation == "-":
        sub(n1,n2)
        n3 = sub(n1,n2)
        print(f" {n1} - {n2} = {n3}")
    elif operation == "*":
        mul(n1,n2)
        n3 = mul(n1,n2)
        print(f" {n1} * {n2} = {n3}")
    elif operation == "/":
        divi(n1,n2)
        n3 = divi(n1,n2)
        print(f" {n1} / {n2} = {n3}")
    

    cntue_cal = input("Type 'y' to continue calculating with " + str(n3) + ", or type 'n' yo start a new calculation.")

    if cntue_cal == 'y':
        calculation_on = True
        count = count +1
    
    elif cntue_cal == 'n':
        calculation_on = False
        os.system("cls")
        print(f" {n1} {operation} {n2} = {n3}")

    

