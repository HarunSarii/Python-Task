#task 2
age = input("Are you a cigarette addict older than 75 years old?: ")
chronic = input("Do you have a severe chronic disease?: ")
immune = input("Is your immune system too weak?: ")
if age.lower() == "yes":
    age = True
else:
    age = False

if chronic.lower() == "yes":
    chronic = True
else:
    chronic = False

if immune.lower() == "yes":
    immune = True
else:
    immune = False

result = age or chronic or immune

if result:
    print("You are in risky group!")
else:
    print("You are not in risky group!")

