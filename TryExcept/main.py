"""
Imagine you have a list of strings.
Print the strings in this list that contain only numbers to the screen.
Don't forget to use try,except blocks while doing this.
"""

liste1 = ["345","NewYork","324a","14","Furkan"]
for i in liste1:
    try:
        i = int(i)
        print(i)
    except:
        pass

"""
Write a function that queries whether a number is even or not.
This function returns this value with *return* if the number is even.
However, if the number is odd, the function will throw a *ValueError* error with *raise*.
Then, define a list containing even and odd numbers and scroll through the list and print only the even numbers on the screen.
"""
def isEven(x):
        if(x % 2 == 0):
            return x
        else:
            raise ValueError

liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,231,234,5431,45312]
for i in liste:
    try:
        print(isEven(i))
    except:
        pass
