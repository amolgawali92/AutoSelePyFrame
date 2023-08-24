# Create string Variables

#Examples 1--Ways of creating variables

s="welcomes"
s='welcom'
s=str("welcome")
s=str('welcome')


# Creating empty string variables
name=""
name=''
name=str()

# Example-2-- Ways of creating string variables
# mutable-cannot change the value of variable.
# immutable - can change the value of the variable
# string is immutable
# If the value is changed after update then it is immutable.

str1= "welcome"   #2360453320496
print(id(str1))

str1=str1+'hi'
print(id(str1))   #2360454959280


# Example 3-  +  and  *  with string

str="welcome"
print(str+"hi")   #concatenation/joining
print(str*3)   #hihihi

# Slicing





