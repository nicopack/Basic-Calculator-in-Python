def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    				  #Creating functions for operations
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:	#Setting loop
	choice = input("Write the calculation you want to make(+, -, *, /) : ")   #Asking what operation to perform

	if choice == "+" or choice == "-" or choice == "*" or choice == "/":
		try:
			num1=int(input("Write the first number: "))
			num2=int(input("Write the second one: "))
		except ValueError:
			print("Please put a number inside the gap.")   #Correcting if there wasn't given a number
			continue

		if choice == "+":
			print(num1, "+", num2, "=", add(num1, num2))   #Addition

		elif choice == "-":
			print(num1, "-", num2, "=", subtract(num1, num2))   #Subtraction

		elif choice == "*":
			print(num1, "*", num2, "=", multiply(num1, num2))   #Multiplication

		elif choice == "/":
			print(num1, ":", num2, "=", divide(num1, num2))   #Division
			
		next_calculation = input("Do you want to do other calculations(yes/no): ")   #Asking to perform other calculations

		if next_calculation == "no":
			break   #Breaking loop
	else:
		print("Invalid input!")   #Correcting if there wasn't given one of the operations
