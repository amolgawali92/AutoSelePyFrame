# input ()- input () is used to take the input from the user

num1=input("Enter your First number")
num2=input("Enter your Last Number")

print(type(num1)) #  From given iput from console window , the data type is always consider as a string

# To convert data type string to integer follow below approach

#Approach-1
num1=int(input("Enter your First number:"))
num2=int(input("Enter your Last Number:"))

print(type(num1))  # for int type
print(type(num2))  # for int type

print(num1+num2)

# Approach-2
num1=int(input("Enter your First number:"))
num2=int(input("Enter your Last Number:"))

print(int(num1)+int(num2))  # convert string to int data type


