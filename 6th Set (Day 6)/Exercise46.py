#Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program. 

num = int(input("Please enter a number: "))

while num <= 5:
    num = int(input("Please enter a number: "))

print("The last number you entered was", num)