# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(24))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_num(num):
    if num % 2 == 0:
        print('Even!')
    else:
        print('Odd')

print(even_num(20))



