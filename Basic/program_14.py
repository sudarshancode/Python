'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num =int(input("Enter any real number:"))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")