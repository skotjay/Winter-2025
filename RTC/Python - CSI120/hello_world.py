def is_prime(n):                        #This function checks if a number is prime.
    if n <= 1:                          #If the number is less than or equal to 1, it is not prime.
        return False                    #Return False.
    if n == 2:                          #If the number is 2, it is prime.
        return True                     #Return True.
    if n % 2 == 0:                      #If the number is even, it is not prime.
        return False                    #Return False.
    i = 3                               #Start at 3.
    while i * i <= n:                   
        if n % i == 0:                  #If n is divisible by i.
            return False                #Return False.
        i += 2                          #Only check odd numbers. #Increment i by 2.
        return True
    
#Validating prime numbers took a lot more steps without using the RANGE function, which would have been easier.

count = 0                               #Initialize count to 0.
num = 2                                 #Starts output at 2.         
primes_found = 0                        #Initialize primes_found to 0.

user_input = int(input("How many prime numbers would you like? "))

while primes_found < user_input:        #While the number of primes found is less than the user input.
    if is_prime(num):                   #If the number is prime as defined above.
        print(num)                      #Print the number.
        primes_found += 1               #Increment the number of primes found and continue the loop.
    num += 1                            #Increment the number by 1 and continue the loop.
