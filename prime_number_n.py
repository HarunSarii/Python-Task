#n prime number

prime = []

n = int(input("Enter a number "))    

for number in range(1,n):  
   if number > 1:  
       for i in range(2,number):  
           if (number % i) == 0:  
               break  
       else:  
           prime.append(number)
            
print(prime)

