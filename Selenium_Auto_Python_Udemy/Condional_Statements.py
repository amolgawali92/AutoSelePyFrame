# Conditional Statements
# if  if..else    elif

# Example1: Print a person is eligible for vote or not

age=21
if age>=18:
    print("Person is eligible for voting")

else:
    print("Person is not Eligible for vote")

# Example-2
# Find a number even/odd   num%2=0

num=10
if num%2==0:
    print("Number is even")  # if condition is True then execute this statement.
else:
    print("Number is odd")   # if condition is false then execute this statement.



# Example-3

if 1:  # 1 is representing a True and 0 is representing a False.# if statement is always accepet boolean values
    print("one")
else:
    print("Not one")


# elif
# Example- Multiple conditions using elif

weekno=7

if weekno == 1:
    print("Sunday")

elif weekno == 2:
    print("Monday")

elif weekno == 3:
    print("Tuesday")

elif weekno == 4:
    print("Wednesday")

elif weekno == 5:
    print("Thursday")

elif weekno == 6:
    print("Friday")

if weekno == 7:
    print("Saturday")


# Example - Given number is positive or negative

num=0

if num<=0:
    print("No is Negative")
else:
    print("No is Positive")














