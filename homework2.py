'''a = input("enter a name:")

if type(a) == str:
    if a == "sanskriti":
        b = input("enter the address:")
        if b == "kathmandu" or b == "pokhara":
            print(f"{a} lives in {b}")
        else:
            print("invalid input")
    else:
        print("invalid input") '''


name = input("enter your name:")
ad = input("enter your address:")

if type(name) == str and type(ad) == str:
    print(f"{name} lives in {ad}")
else:
    print("invalid input")