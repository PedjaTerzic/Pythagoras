'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python pythagoras.py
    or if it doesn't work use this one:
        python3 pythagoras.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''
import sympy
print("                        ***** PYTHAGORAS *****\n\n\n")
while True:
    p=int(input("Enter a prime number : "))
    if not(sympy.isprime(p)):
        print("You must enter a prime number")
    else:
        if p==2:
            print("4*"+str(p)+"+1 is composite")
        elif p==3:
            print("4*"+str(p)+"+1 is prime")
        elif p%6==5:
            print("4*"+str(p)+"+1 is composite")
        elif (4*p+1)%5==0:
            print("4*"+str(p)+"+1 is composite")
        else:
            if pow(2,2*p,4*p+1)==4*p:
                print("4*"+str(p)+"+1 is prime")
            else:
                print("4*"+str(p)+"+1 is composite")
    try_again = ""
    # Loop until users opts to go again or quit
    while not(try_again == "1") and not(try_again == "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.") 
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break