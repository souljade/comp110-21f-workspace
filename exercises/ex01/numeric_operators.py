"""Trying to learn how to play with numbers!"""

__author__ = "730327594"

left_side: str = input("enter the first number: ")
right_side: str = input("enter the second number: ")

new_left = int(left_side)
new_right = int(right_side)

print(left_side + " ** " + right_side + " is " + str(new_left ** new_right)) 
print(left_side + " / " + right_side + " is " + str(new_left / new_right))
print(left_side + " // " + right_side + " is " + str(new_left // new_right))
print(left_side + " % " + right_side + " is " + str(new_left % new_right))