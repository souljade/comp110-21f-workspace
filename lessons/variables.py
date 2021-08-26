"""example diagram problem"""

"""This is initializing the variable... naming it and establishing its presence in my stack-- globals"""
age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2041: int = 2041 - year + age
print("In 2041, you will be " + str(age_in_2041))


"""reasigning the variables to new value with the expression below. from now on, the program will use the new variable value!"""
age = age + 1
year = year + 1
print("In " + str(year) + ", youll be " + str(age))