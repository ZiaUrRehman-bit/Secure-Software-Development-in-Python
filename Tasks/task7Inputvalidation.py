try:
    age = int(input("Enter your age: "))
    print("Next year you will be:", age + 1)
except ValueError:
    print("Invalid age input")
