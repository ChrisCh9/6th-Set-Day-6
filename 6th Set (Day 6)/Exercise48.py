#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. 

color = input("Please enter your favourite color: ")

if color == "RED" or color == "Red" or color == "red":
    print("I like red too")

else:
    print("I dont like", color, "I prefer red")