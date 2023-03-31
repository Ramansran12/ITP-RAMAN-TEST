#RAMANDEEP SINGH
#id 22076254
#creating takeINPUT()
def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    opt = input("Enter opt (+,-,*,/): ")
    return num1, num2, opt

#creating displayResult
def displayResult():
    num1, num2, opt = takeInput()

    if opt == '+':
        result = num1+num2
        formula = f"{num1}+{num2}={result}"
    elif opt == '-':
        result = num1-num2
        formula = f"{num1}-{num2}={result}"
    elif opt == '*':
        result = num1*num2
        formula = f"{num1}*{num2}={result}"
    elif opt == '/':
        result = num1/num2
        formula = f"{num1}/{num2}={result}"
    else:
        print("Invalid opt")
        return

    print(formula)

displayResult()