#Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total. 

total = 0

num1 = int(input("Please enter a number: "))

num2 = int(input("Please enter a number: "))

total = num1 + num2

choice = input("Select y: to continue or n: to stop ")

while choice == "y":
    
    num3 = int(input("Please enter a number: "))
    
    total += num3

    choice = input("Select y: to continue or n: to stop ")

print("The total is: ", total)