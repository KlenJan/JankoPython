age = input("How old are you? ")
if not age:
    print("you didnt enter anything")
else:
    age = int(age)
    if age >= 21:
        print("come in and drink")
    elif age < 18:
        print("you are too young")
    else:
        print("you can come but no drinking")
