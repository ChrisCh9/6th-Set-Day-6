#Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”.

answer1 = input("Please tell me if it was raining or not: ")

answer1.lowercase()

answer2 = input("Please tell me if it was windy or not: ")

answer2.lowercase()

if answer1 == "yes" and answer2 == "yes":
    print("It is too windy for an umbrella")

elif answer1 == "yes" and answer2 == "no":
    print("Take an umbrella")

else:
    print("Enjoy your day")