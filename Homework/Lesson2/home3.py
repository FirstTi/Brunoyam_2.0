def home3():
    name = input("What is your name?")
    age = input("How old are you?")
    live = input("Where are you live?")
    return name, age, live

def home33():
    name, age, live = home3()

    print(f"This is your name: {name}")
    print(f"This is your age: {age}")
    print(f"You live in {live}")
    

while True:
    home33()
    break