#ARMSTRONG NUMBER:
    
number = input("enter a positive integer number: ")
if (set(number)&set("0123456789")==set()) :
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    number = int(number)
    float_check = isinstance(number, float)
    if (number < 0 or float_check):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    else:
        sum = 0
        for i in str(number):
            sum += int(i)**len(str(number))
        if sum == number:
            print(number, "is an Armstrong number")
        else:
            print(number, "is not an Armstrong number")
    

