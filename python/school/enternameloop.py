def func():

    name = input("What is your name? ")
    num = int(input("Enter a number! "))

    for i in range (num):
        print(name)

    replay = input("Do you want to play again? ")

    if (replay == "y" or replay == "Y"):
        func()


func()

