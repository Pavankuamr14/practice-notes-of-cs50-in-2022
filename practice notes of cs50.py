#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def level_one():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correct_answer = num1 + num2
    print(f"Level: {num1} + {num2} = ", end="")
    return correct_answer

def level_two():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    correct_answer = num1 + num2
    print(f"Level: {num1} + {num2} = ", end="")
    return correct_answer

def level_three():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    correct_answer = num1 + num2
    print(f"Level: {num1} + {num2} = ", end="")
    return correct_answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", correct_answer)

def main():
    for _ in range(10):
        level = random.randint(1, 3)
        if level == 1:
            correct_answer = level_one()
        elif level == 2:
            correct_answer = level_two()
        else:
            correct_answer = level_three()

        user_answer = int(input())
        check_answer(user_answer, correct_answer)

if __name__ == "_main_":
    main()


# In[6]:


import random

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Final Score: {score}")

def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input not in [1, 2, 3]:
                raise ValueError
            else:
                break
        except (ValueError, TypeError):
            pass
    return user_input

def generate_integer(level):
    question = 0
    score = 0
    while question < 10:
        range1 = -1
        range2 = -1
        if level == 1:
            range1 = 0
            range2 = 9
        elif level == 2:
            range1 = 10
            range2 = 99
        elif level == 3:
            range1 = 100
            range2 = 999
        x = random.randint(range1, range2)
        y = random.randint(range1, range2)
        count = 0
        while count < 3:
            try:
                value = int(input(f'{x} +{y} =',end=''))
                if value == x + y:
                    score += 1
                    question += 1
                    break
                else:
                    print("EEE")
                    count += 1
            except (ValueError, TypeError):
                print("EEE")
                count += 1
        else:
            print(f'{x} +{y} = {x + y}')
            question += 1

    return score

if __name__ == "_main_":
    main()


# In[ ]:





# In[ ]:





# In[ ]:


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
course=["python","css","java"]
info={"name":"pav","age":21}
student_info(*course,**info)
    


# In[ ]:





# In[3]:


user_input=input()
def items(user_input):
    count=0
    found=True
    items={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
#     while True:
    if user_input in items:
        count+=items[user_input]
        print(count)
    else:
        pass
    return count
            
    
# main()


# In[ ]:


try: 
    inp=input()
exceptEOFError:
    


# In[21]:


def main():
    var=us()
    for i in range(len(var)):
        print(f"{i} {var[i]}")
    
def us():
    while True:
        lst=[]
        try:
            user=input()
            raise EOFError
            if user.upper() not in lst:
                lst.append(user)
            else:
                pass
        except EOFError:
            break
    return lst
            
            
    
    
main()


# In[ ]:


def get_input():
    while True:
        try:
            us=input()
        except EOFError:
            break
        
    return us
get_input()


# In[ ]:


def get_input():
    user_input = ""  # Initialize an empty string to store user input
    while True:  # Continue reading input until the user presses Enter
        try:
            line = input()
            if not line:  # If the user presses Enter without typing anything
                break
            user_input += line + "\n"  # Append the input to the existing user_input
        except EOFError:
            break
#     return line.strip()
    return user_input.strip()  # Remove trailing newline characters and return the input

user_input = get_input()


# In[16]:


def get_input():
    user_input = ""  # Initialize an empty string to store user input
    while True:  # Continue reading input until the user presses Enter
        try:
            line = input().strip()
            if not line:  # If the user presses Enter without typing anything
                break
            user_input += line+"\n"  # Append the input to the existing user_input
        except EOFError:
            break
    return user_input  # Remove trailing newline characters and return the input

user_input2 = get_input()
print("User input:")
print(user_input2)


# In[2]:


us=int(input("ENTER length "))
lst=[]
for i in range(us):
    number=int(input(f"ENTER THE VALUE {i} "))
    lst.append(number)
print(sum(lst))


# In[5]:


def main():
    us=us=int(input("ENTER NUMBERS WILL GIVE TO DO SUM "))
    rl=addition(us)
    return max(rl)
    
def addition(us):
    lst=[]
    for i in range(us):
        number=int(input("ENTER A VALUE "))
        lst.append(number)
    return lst
main()


# In[9]:


num=100
num1=100
add=200
us=int(input("enter a value"))
us=int(input("enter a value"))
num=100-us
num1=100-us
print(add-())


# In[ ]:





# In[ ]:


def coke(s):
    price=50
    us=int(input(f"Amount Due: {price}")
    if us!=price:
        print(f"Insert Due: {price-us})
    coke()


# In[ ]:


import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)

titlecase("they're bill's friends.")
# "They're Bill's Friends."


# In[ ]:


# note='st' means start
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
# check length of the s should be min=2 and max=6
    if len(s) >= 2 and len(s) <= 6:
# checking that whether the s is alpha or alphanum(a text that contains both alphabets and digits)
        if s.isalpha():
        # checking that if the input s contains only alphas.and their is no digit  then we pass that is_valid_start(s) funtion
        # if the text st with digit
            return is_valid_start(s)
        elif s.isalnum():
            return is_valid_start(s) and is_valid_end(s)
    return False

def is_valid_start(s):
    # if the text st with 2 words in the text then it is vaild and return that parameter
    # else return invaild
    return s[:2].isalpha()

def is_valid_end(s):
    # if the text contain both alphabets and digits
    # we need to check this conditions
# no space or punctuation marks are alloweds'
# NOTE:-last word of the text strictly should a digit( to vaild)
# NOTE:- the starting digit should not be "0" it can be neither of the" number"
# to check that condition i consider a list if we found the number inn the text we will add it to the list
# if first item of the list is "0" its invaild return s
    found=False
                
main()


# In[4]:


# s=input()
# rs=s.title()
def main():
    s=input()
    rs=s.title()
    check(count)
    print(f"${count}")
def check(rs):
    items={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    while True:
        if rs in items:
            count=+items[rs]
        elif rs==cntrl+d:
            break
    return count
main()
    


# In[ ]:


def check(rs):
    items={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    while True:
        if rs in items:
            count=+items[rs]
        elif rs==ctrl+d:
            break
    return count
check("burrito")


# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>2 and len(s)<=6:
        ls=["0","1","2","3","4","5","6","7","8","9","a","b"]
        for i in ls:
            if i in s[0:]:


main()


# In[ ]:


# note='st' means start
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
# check length of the s should be min=2 and max=6
    if len(s) >= 2 and len(s) <= 6:
# checking that whether the s is alpha or alphanum(a text that contains both alphabets and digits)
        if s.isalpha():
        # checking that if the input s contains only alphas.and their is no digit  then we pass that is_valid_start(s) funtion
        # if the text st with digit
            return is_valid_start(s)
        elif s.isalnum():
            return is_valid_start(s) and is_valid_end(s)
    return False

def is_valid_start(s):
    # if the text st with 2 words in the text then it is vaild and return that parameter
    # else return invaild
    return s[:2].isalpha()

def is_valid_end(s):
    # if the text contain both alphabets and digits
    # we need to check this conditions
# no space or punctuation marks are alloweds'
# NOTE:-last word of the text strictly should a digit( to vaild)
# NOTE:- the starting digit should not be "0" it can be neither of the" number"
# to check that condition i consider a list if we found the number inn the text we will add it to the list
# if first item of the list is "0" its invaild return s

#     lst=[s[i] for i in range(len(s)) if s[i].isdigit()]
    for i in range(len(s)):
        if s[i].isdigit:
            digit_ind=s.index(s[i])
            break
    if s[digit_ind:].isdigit():
        return s[-1].isdigit() and s[digit_ind] != '0'

    # return s[-1].isdigit() and s[-2:].isdigit()

main()


# In[ ]:





# In[ ]:


# note='st' means start
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
# check length of the s should be min=2 and max=6
    if len(s) >= 2 and len(s) <= 6:
# checking that whether the s is alpha or alphanum(a text that contains both alphabets and digits)
        if s.isalpha():
        # checking that if the input s contains only alphas.and their is no digit  then we pass that is_valid_start(s) funtion
        # if the text st with digit
            return is_valid_start(s)
        elif s.isalnum():
            return is_valid_start(s) and is_valid_end(s)
    return False

def is_valid_start(s):
    # if the text st with 2 words in the text then it is vaild and return that parameter
    # else return invaild
    return s[:2].isalpha()

def is_valid_end(s):
    # if the text contain both alphabets and digits
    # we need to check this conditions
# no space or punctuation marks are alloweds'
# NOTE:-last word of the text strictly should a digit( to vaild)
# NOTE:- the starting digit should not be "0" it can be neither of the" number"
# to check that condition i consider a list if we found the number inn the text we will add it to the list
# if first item of the list is "0" its invaild return s
    found=False
    temp=''
    for x in range(len(s)):
        if s[x].isdigit():
            index=s.index(s[x])
            found=True
        if found==True:
            for j in range(index, len(s)):
                if s[j].isdigit():
                    return s[-1].isdigit() and s[index] != '0'
                found=False
            
            
main()


# In[ ]:


# 2 letter at beg
# digits at end
# >=2 and <=6
# no digit should be in text
# no space or punctuation marks are alloweds'
# CS50:-VALID
# CS05:-INVAILD
s=input("")
#aa222
#AA567SA
#HELO REY
#AAV067
length_of_s=len(s)
if s[0].isalpha() and s[1].isalpha() and s[-1].isdigit():
#     print("vaild")
    pass
else:
    if len(s)>3:
        for i in range (length_of_s+2,length_of_s-2):
            if s[i].isdigit() or s[i]==" " or s[i]=="," or s[i]==".":
                print("INVAILD")    
        print("Valid")


# CORRECT CODE IS BELOW ONE FOR VAILD PALTES
# 

# In[ ]:



# note='st' means start
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) >= 2 and len(s) <= 6:

        if s.isalpha():
        # checking that if the input s contains only alphas.and their is no digit  then we pass that is_valid_start(s) funtion
        # if the text st with digit
            return is_valid_start(s)
        elif s.isalnum():
            return is_valid_start(s) and is_valid_end(s)
    return False

def is_valid_start(s):
    # if the text st with 2 words in the text then it is vaild and return that parameter
    # else return invaild
    return s[:2].isalpha()

def is_valid_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            ind=s.index(s[i])
            break
    if s[0:ind].isalpha and s[ind+1:].isdigit():
        return s[ind] != '0'
        

main()


# In[ ]:


s='cs50p2'
for i in range(len(s)):
    if s[i].isdigit:
        ind=s.index(s[i])
        break

print(s[0:ind])


# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if len(s)>2 and len(s)<=6:
        if s.isalpha() or s[0].isalpha() and s[1].isalpha() and s[-1].isdigit() and s[2:len(s)-2].isalpha():
            return(s)
         
#             print("Valid")
#             break
#         elif s[0].isalpha() and s[1].isalpha() and s[-1].isdigit() and s[2:len(s)-2].isalpha():
#             pass
#             print("Valid")
#         else:
#             print("Invalid")
#     return(s)
main()


# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha() and s[-1].isdigit() and s[2:-1].isalpha():
            return True
    return False

main()


# In[20]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return is_valid_start(s)
        elif s.isalnum():
            return is_valid_start(s) and is_valid_end(s)
    return False

def is_valid_start(s):
    return s[:2].isalpha()

def is_valid_end(s):
    
#     lst=[i if s[i].isdigit()]
#     for i in range(len(s)):
    lst=[s[i] for i in range(len(s)) if s[i].isdigit()]
    return s[-1].isdigit() and lst[0] != '0'

main()


# In[ ]:


s='cs50'
lst=[s[i] for i in range(len(s)) if s[i].isdigit()]
lst


# In[ ]:


D="CS50"
D.isalnum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    join=""
    i=0
    len(s)
    if len(s)>2 and len(s)<=6:
        while i<len(s):
            if s[i].isalpha():
#                 join+=s[i]
                
                return s
                i+=1
            elif s[i].isdigit():
                if s[i]=="0" and s[i-1].isalpha():
                    print("Invaild")
                else:
                    return s
                if s[i+1].isalpha():
                    return s
                i+=1
            else:
                return s
        
main()       


# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>2 and len(s)<=6:
        if s.isalnum:
            print("Valid")
        elif s[0].isalpha() and s[1].isalpha() and s[-1].isdigit() and s[2:len(s)].isalpha():
            print("Valid")
            
        else:
            print("Invalid")
#             if s[0].isalpha() and s[1].isalpha() and s[-1].isdigit():
#                 for i in range(len(s)+2,len(s)-2):
#                     if s[i].isdigit():

#                     else:
#                         print("Valid")
#         elif(s[0].isalpha() and s[1].isalpha())
#     print("Invaild")


main()


# In[ ]:


s="HELLO.WORLD"
if s.isalpha():
    print("true")
elif s[-1].isdigit
else:
    print("false")


# In[ ]:


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    join=""
    count=0

    if len(s)>2 and len(s)<=6:
        for i in range(len(s)-1):
            if s[i].isalpha():
                join+=s[i]
                if s[i+1].isdigit():
                    count+=1
                    if count==1 and s[i+1]:
                        s[i+1]!='0'
                        
main()


# In[ ]:


s="hello50"
if s[0].isalpha() and s[1].isalpha() and s[-1].isdigit():
    print("gjhk")


# In[ ]:


s="hello50"
if s[-1].isdigit():
    print("ddsdfs")


# In[ ]:


count=0
price=50
def cokemachine(x):
    print(f"Amount Due: {price}"))
    us_insert_coin=int(input("Insert Coin: "))
    us_amount_due=int(input(f"Amount Due: {price-us_insert_coin}"))
cokemachine(25)


# In[ ]:





# In[ ]:





# In[ ]:


us=input("Item: ").lower()
if us=="apple":
    print("Calories: 130")
elif us=="avocado":
    print("Calories: 50")
elif us=="banana":
    print("Calories: 110")
elif us=="cantaloupe":
    print("Calories: 50")
elif us=="grapefruit":
    print("Calories: 60")
elif us=="grapes":
    print("Calories: 90")
elif us=="honeydew melon":
    print("Calories: 50")
elif us=="kiwifruit":
    print("Calories: 90")
elif us=="lemon":
    print("Calories: 15")
elif us=="lime":
    print("Calories: 20")
elif us=="nectarine":
    print("Calories: 60")
elif us=="orange":
    print("Calories: 80")
elif us=="peach":
    print("Calories: 60")
elif us=="pear":
    print("Calories: 100")
elif us=="pineapple":
    print("Calories: 50")
elif us=="plums":
    print("Calories: 70")
elif us=="strawberries":
    print("Calories: 50")
elif us=="sweet cherries":
    print("Calories: 130")
elif us=="tangerine":
    print("Calories: 50")
elif us=="watermelon":
    print("Calories: 80")
    


# In[ ]:


import pandas as pd


# In[ ]:


us=input("ebter ")
if ".gif" in us:
    print("image/gif")
elif ".png" in us:
    print("image/gif")
elif ".jpg" in us:
    print("image/jpeg")
elif ".jpeg" in us:
    print("image/jpeg")

elif ".pdf" in us:
    print("application/pdf")
# elif ".txt" in us:
    
else:
    print("application/octet-stream")
    


# In[ ]:


us=input("File Name: ").strip()
if ".gif" in us:
    print("image/gif")
elif ".png" in us:
    print("image/png")
elif ".jpg" in us:
    print("image/jpeg")
elif ".jpeg" in us:
    print("image/jpeg")

elif ".pdf" in us:
    print("application/pdf")
elif ".PDF" in us:
    print("application/pd...")
elif ".txt" in us:
    print("text/plain")
elif ".zip" in us:
    print("application/zip")

else:
    print("application/octet-stream")



























# us=input("File Name: ")
# if ".gif" or ".png" in us:
#     print("image/gif")
# elif ".jpg" or ".jpeg" in us:
#     print("image/jpeg")
# elif ".pdf" in us:
#     print("application/pdf")
# # elif ".txt" in us:

# else:
#     print("application/octet-stream")



















# lst=[".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]
# File_Name:=input("File Name: ")
# for i in lst:
#     if i in lst:
#         print(f"{File_Name}/{i}")
#     else:
#         print("application/octet-stream")


# In[ ]:


string = " www.geeksforgeeks.org www. ".strip(" ")
 
# string_new = string.strip(" ")
 
print(string)


# In[ ]:


us=input().lower()
ls=["a","e","i","o","u"]
for i in ls:
    if i in us:
        us=us.replace(i,"")
us


# In[ ]:


user_input=str(input())
print(user_input.


# In[ ]:


user_input=str(input())
size=len(user_input)
print(user_input[::-1])


# In[ ]:


user_input=str(input())
size=len(user_input)
print(user_input[-(size):-1])


# In[ ]:


Write a Python program that prompts the user to 
enter a number and then prints whether the number 
is even or odd. Use comments in your code to explain the logic behind determining the evenness or oddness


of the number.Numeric Data Types and Character Sets:


# In[ ]:


Write a Python program that calculates the sum of all the digits
in a given integer. For example, if the input is 12345, 
the program should output 15.Using Functions and Modules:


# In[ ]:


def solve(*args):
    add=0
    for i in range(*args):
        add+=args[i]
    return add
solve(12,34,566)


# In[ ]:


n=int(input())
add=0
for i in range(n):
    add+=n[i]
print(add)


# In[ ]:


s=1233
print(s[0])


# In[ ]:


Write a Python program that defines a function to 
calculate the factorial of a given number.
Use this function to prompt the user for a number and print its factorial
.Strings Assignment:


# In[ ]:





# In[ ]:


def sum(a,b):
    c = a + b
    #return c
    return(a-b)
sum(2,3)


# In[ ]:


#shopping_list = [‘milk’, ‘eggs’, ‘cookies’, ‘bread’] 
# list of strings

favorite_words = [22, 'hello', 43, False] 
# list of mixed data types
favorite_words.remove(22)
favorite_words.insert(1,"frst")
print(favorite_words)

#books = [‘maths’, [‘chem’, ‘phy’], ‘biology’] 
# we can even have a list inside a list


# In[ ]:


numbers = [2,342,99,15,43,23,22]
for num in numbers: # iterating through each number#0,1,
	num = num + 2#2,3,
print(num)

# Output: [2, 342, 99, 15, 43, 23, 22]


# In[ ]:


for i in range(1,6):
    for j in range(1,6):
#         print(i+1,end=" ")
        print(i*j,end='  ')
        
    print()


# In[ ]:


for i in range(1,6):
    print(i)


# In[ ]:


# size=int(input("sze 0r columns"))
size=3
for i in range(0,size):
    
    for j in range(1,usr+1):
        usr=int(input())
        for z in range(size):
            
            print(z,end=' ')
        print()


# ## 

# In[ ]:


rane=int(input())
for s in range(rane):
    for z in range(size):
        user_input=int(input())
    
        for i in range(1,user_input+1):
            for j in range(size):
                print(i,end='')
            print()


# In[ ]:


subbu=int(input())#4
for s in  range(subbu):#0,1,2,3
    user_input=int(input())#4
    for i in range(1,user_input+1):#1,2,3,4
        for j in range(3):
            print(i,end='')
        print()


# In[ ]:


subbu=int(input())
for s in  range(subbu):
    print(s)


# In[ ]:


def least_difference(a, b, c):
    diff1 = abs(a - b)#1-10=-9
    diff2 = abs(b - c)#10-100=-90
    diff3 = abs(a - c)#1-100=-99
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
    
#1-10=-9
#10-10=0
#1-10=-9

#5-6=-1
#6-7=-1
#5-7=-2
    
    
    
    
    


# In[ ]:


3.00000000000000009==3


# In[ ]:


df=pd.read_csv('aug_train.csv')


# In[ ]:


def solve(num,st):
    temp=st[num]
    return temp
solve(2,'frdu')


# In[ ]:


def equal_num(num,num2):
    if(num==num2):
        return equal_num
    elif(num>num2):
        return "num is greater"
    elif(num2>num):
        return "num2 is greater"
    else:
        return equal_num
equal_num(5,3)


# In[ ]:


def num (num):
    if(num%2==0):
        print("even number")
    else:
        print("odd number")
num(3)
    


# In[ ]:


def solve(number_checked,starting_number,ending_number):
    if(number_checked in range(starting_number,ending_number)):
        print("u entered number is in  given range ")
    else:
        print("u entered number is not in given range ")
solve(4,1,5)


# In[ ]:


def solve(num1, num2,num3):
    if num1%num2 and num1%num3 :
        print(f"{num1} is either divisible by {num2} or divisible by {num3}")
    else:
        print(f"{num1} is neither divisible by {num2} nor divisible by {num3}")
solve(8,2,4)
    


# In[ ]:


def solve(num1,num2,num3):
    if num1%num2==0 and num1%num3==0:
        return "true"
    else:
        return "false"
solve(8,2,4)


# In[ ]:


def party (number_of_choco,is_its_weekend):
    if number_of_choco in range(20,41) and is_its_weekend=="false":
        print("hurray! party is done successfully")
    elif number_of_choco>=20 and is_its_weekend=="true":
        print("hurray! party is done successfully")
    else:
        print("sorry to say that party is misfired")
party(50,"false")


# In[ ]:


def sweets(score,its_your_bday):
    if its_your_bday=="false":
        if score in range (81,100):
            print("u will recieve  2 sweeties")
        elif score in range (61,80):
            print("u will recieve 1 sweety")
        else:
            print(" sorry to that u did not recived any sweeties from u mom ,better luck next time !")
    else:
        score+=5
        if score in range (81,100):
            print("u will recieve  2 sweeties")
        elif score in range (61,80):
            print("u will recieve 1 sweety")
        else:
            print(" sorry to that u did not recived any sweeties from u mom ,better luck next time !")
        
sweets(65,"false")
    


# In[ ]:


def sweets(score,its_your_bday):
    if its_your_bday!="true":
        score+=5
    if score in range (81,100):
        print("u will recieve  2 sweeties")
    elif score in range (61,80):
        print("u will recieve 1 sweety")
    else:
        print(" sorry to that u did not recived any sweeties from u mom ,better luck next time !")
        
sweets(65,"false")


# In[ ]:


def dwight(target, small_brick, big_brick):
    if target % (big_brick*2) == 0 or target % small_brick == 0 or target == big_brick*2 + small_brick:
        print("possible")
    else:
        print("impossible")

dwight(5, 2, 1)


# In[ ]:


def game(player1_value,player2_value):
    if(player1_value>player2_value and player1_value<=21):
        print("player1 won the match")
    elif(player2_value>player1_value and player2_value<=21):
        print("player2 won the match")
    else:
        print("both lost the match")
game(19,19)


# In[ ]:


def twist(num1,num2):
    
    if(num1==num2):
        print("0")
        rem1=num1%6
        rem2=num2%6
        if(rem1==rem2):
            if num1<num2:
                print(num1)
            else:
                print(num2)
                
        else:
            print("0")
    
twist (35,28)
        


# In[ ]:


def solve (lst):
    for i in lst:
        print(i,end=" ")
solve ([22,34,5,67,87,64])


# In[ ]:


lst=[22,34,5,67,87,64]
for i in range(len(lst)):
    print(lst[i],end=" ")


# In[ ]:


lst=[22,34,5,67,87,64]
for i in range(len(lst)):
    if lst[i]%2==0:
        print("even number")
    else:
        print("odd number")
    


# In[ ]:


def vowel(lst):
    vwl=["a","e","i","o","u"]
    words=lst.split()
    temp=[]
    
    for word in words:
        if(word[0].lower() in vwl):
            temp.append(word)
    return temp
vowel("hi i am k.pavansaikumar")


# In[ ]:


def vowel(s):
    vwl = ["a", "e", "i", "o", "u"]
    words = s.split()
    result = []
    
    for word in words:
        if word[0].lower() in vwl:
            result.append(word)
    
    return result

print(vowel("hi i am k.pavansaikumar"))


# In[ ]:


class clg:
    def __init__(self,strength,code,room_num,girls,boys):
        #self.branch=branch
        self.strength=strength
        self.code=code
        self.room_num=room_num
        self.girls=girls
        self.boys=boys

    def acess(self):
        #print("BRANCH NAME:-",self.branch)
        print("stength of class",self.strength )
        print("BRANCH CODE",self.code)
        print("ROOM NUMBER",self.room_num)
        print("GIRLS STRENGTH IN THAT BRANCH",self.girls)
        print("BOYS STRENGTH IN THAT BRANCH",self.boys)


csm=clg(125,"rom2","B101",50,75)
csm.acess()

#obj=clg()
#obj.acess()




# In[ ]:


for i in range(1,10):
    print('*')


# In[ ]:


for i in range(1,10):
    print(i*'*')


# In[ ]:


for i in range(1,10):
    for j in range(i):
        print(j*"*")


# In[ ]:


for i in range(1,10):
    for j in range(i):
        print(f'*{j}')


# In[ ]:


for i in range(5):
    print(i)


# In[ ]:


for i in range(1,10):
    for j in range(1,10):
        print(f'*{i}',end=" ")


# In[ ]:


n=6
for i in range(n+1):
    for j in range(n+1):
        if i==j or i+j==n:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()


# In[ ]:


n=6
for i in range(n+1):
    for j in range(n+1):
        if j==0 or i==0:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()


# In[ ]:


n=6
for i in range(n+1):
    for j in range(n+1):
        if j==0 or i==0 or j==n or i==n:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()


# In[ ]:


n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


# In[ ]:


temp=[]
n=int(input("enter size of list elements"))
for i in range(0,n):
    numbers=int(input("enter number nows"))
    temp.append(numbers)

print(temp)
for i in range(0,n):
    temp2=temp[0]
    temp[0]=temp[n-1]
    temp[n-1]=temp2
print(temp)


# In[ ]:


lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# In[ ]:


var=lst[0:4]


# In[ ]:


len(lst)


# In[ ]:


print(var)


# In[ ]:


n=5
# for i in range(len(lst)):
#     print(lst[0:n])
i=0
while i in range(len(lst)):
    print(lst[0:i])
    i+=n
print()


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n])
    i+=n
    n+=n


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=5
i=0
while i <=len(st):
    print(st[i:n])
    i+=5
    n+=5


# In[ ]:


temp=[]
n=int(input("enter size of list elements"))
for i in range(0,n):
    numbers=int(input("enter number numbers now"))
    temp.append(numbers)

print(temp)
for i in range(0,n):
    temp2=temp[0]
    temp[0]=temp[n-1]
    temp[n-1]=temp2
print(temp)


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n+1])
    i+=n
    n+=n


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n])
    i+=n
    n+=n


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n])
    i+=n
    n+=n
    


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n])
    i+=n
    n+=n


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=4
i=0
while i <=len(st):
    print(st[i:n])
    i+=4
    n+=4


# In[ ]:


st="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=int(input())
i=0
while i <=len(st):
    print(st[i:n])
    i+=n
    n+=n
    


# In[ ]:


###       ALL()---->FUCTION

lst=['1','3',1,0]
print(all(lst))
tu=('3',1,0,0)
print(all(tu))
dic={1:"jbkj",0:"hjbh"}
print(all(dic))
dic={1:"jbkj",1:"hjbh"}
print(all(dic))
#return if all items are true


# In[ ]:


###       ANY()------>FUNCTION
lst=[0,0,False]
print(any(lst))
tu=('3',1,0,0)
print(any(tu))
dic={0:"jbkj",0:"hjbh"}
print(any(dic))
dic={1:"jbkj",1:"hjbh"}
print(any(dic))
#TO RETURN FALSE ALL ITERABLE OBJECTS SHOULD BE FALSE
#OTHERWISE IT RETURN TRUE


# In[ ]:


x = ascii("My name is Ståle")


# In[ ]:


x


# In[ ]:


v=8
print(bin(v))


# In[ ]:


v=8
print(bytes(v))


# In[ ]:


x = 5

print(callable(x))


# In[ ]:


def x():
    pass
print(callable(x))


# In[ ]:


print(chr(98))


# In[ ]:





# In[ ]:


mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict[0])
print(x)


# In[ ]:


lst=[0,1,1]
print(any(lst))


# In[ ]:


lst[0]


# In[ ]:



# 1.	Write a program to check whether the last digit of a number(entered by user ) is divisible by 3 or not.
user_input=int(input())
user_input=str(user_input)
lst=[]
lst.append(user_input)
if int(lst[-1])%3==0:
    print("DIVISIBLE")
else:
    print("NOT")


# In[ ]:


333//3


# In[ ]:


user_input=int(input())
last_digit=user_input%10
if last_digit%3==0:
    print("yes")
else:
    print("no")


# In[ ]:


113%10


# In[ ]:


user_input=int(input())
if user_input%10%3==0:
    print("YES")
else:
    print("No")


# In[ ]:


user_input=int(input())
digits=[int(digit) for digit in str(user_input)]
if digits[-1]%3==0:
    print("YES")
else:
    print("NO")


# In[ ]:


user_input=int(input())
temp=0
temp2=0
if user_input<=100:
    print("no charges")
elif user_input>100 and user_input<200:
    temp=user_input-100
    print(temp*5)
elif user_input>200:
    temp=user_input-100
    print(temp*5)
    temp2=user_input-200
    print(temp*5+temp2*10)
    


# In[ ]:


user_input=int(input())
if user_input>=18:
    print("yes")
else:
    print("NO")
    


# In[ ]:


user_input=int(input())
if user_input>100000:
    cost=user_input*0.15
    print(cost)
elif user_input>50000 and user_input<=100000:
    cost=user_input*0.1
    print(cost)
elif user_input<=50000:
    cost=user_input*0.05
    print(cost)


# In[ ]:


15/100


# In[ ]:


10/100


# In[ ]:


5/100


# In[ ]:


user_input=str(int(input()))
dic={'1':'sunday','2':'monday','3':'tuesday','4':'wednesday','5':'thursday','6':'friday','7':'saturday'}
if user_input in dic:
    print()


# In[ ]:


user_input=int(input())
lst=["","sunday","monday","tuesday","wednesday","thusday","friday","saturday"]
if user_input==0:
    print("enter value getter than 0")
else:
    print(lst[user_input])


# In[ ]:


user_input=str(int(input()))

num=[int(i) for i in user_input]
if len(num)==3:
    print("yes")
else:
    print("no")


# In[ ]:


user_input=str(int(input()))
dic={'1':'sunday','2':'monday','3':'tuesday','4':'wednesday','5':'thursday','6':'friday','7':'saturday'}
if user_input in dic:
    print(dic[user_input])
else:
    print("U HAVE NOT ENTERED THE NUMBER B/w 1 to 7")


# In[ ]:


key_size=int(input())
dic={}
for i in range (key_size):
    key=input()
    values=input()
    dic.update({key:values})
-dic


# In[ ]:


key_size=int(input())
dic={}
for i in range (key_size):
    key=input()
    values=input()
    dic[key]=values
dic


# In[ ]:


ls={"delhi":"redfort","agra":"Taj Mahal","jaipur":"jai mahal"}
user_input=input().lower()
if user_input in ls:
    print(f"{user_input} is a city and it's monument is {ls[user_input]}")
else:
    print("""the city u entered is not in user_pre_defined_dic ....... 
          u can enter cities  name like DELHI,AGRA,JAIPUR""")


# In[ ]:


# method 2  adding all cities by taking it as user_input and we also take monuments as input from user add will dd these input as key and values to dictonary
# its take size of cities
size_cities=int(input())
# creating a empty dictonary
dic={}
# we should get input as many time as size_cities so we need a iterator
for i in range(size_cities):
    # now its take the cites name
    cities_names=input().lower()
    # again now we take monument of that city 
    monument_name=input().lower()
    # next thing we need to do is we need add the cities_names and monuments_names as key value pair to do these we use .update
    dic.update({cities_names:monument_name})
# now we need to get user_input that is city where we can display it's monument 
print("///////////////////////////////////////////////////")
user_entered_city=str(input()).lower()
#checking that user_entered_input is present in the di8c
if user_entered_city in dic:
    print(dic[user_entered_city])
else:
    print("U ENTERED CITY IS NOT PRESENT IN DICTONARY")


# In[ ]:


#score of TEAM_A
test_case=int(input())
for i in range(test_case):
    team_A=int(input())
    team_B_target=team_A+1
    current_score=int(input())
    to_win_team_B_score_req=team_B_target-current_score
    print(f'for {i+1} test_case required runs{to_win_team_B_score_req}')


# In[ ]:



test_case=int(input())
for i in range(test_case):
    team_A_score=int(input(f"enter the team_A_score  for test_case{i+1}:- "))
    team_B_target=team_A_score+1
    current_score=int(input(f"enter current_score of team_B for test_case {i+1}:-"))
    while current_score<=team_A_score:
        to_win_team_B_score_req=team_B_target-current_score
        print(f'for {i+1} test_case required runs:-{to_win_team_B_score_req}')
        break
    else:
        print("please check the current score of team_B..oops it's greater then score of team_A  ")


# In[ ]:


ls=[]

size=int(input())#user will enter size of list that on  his requirement that means the number of cities or number of  monuments
for i in range(size*2):# i need to store both cities and monuments so i user size*2
    user_input=input()#size batti ikkada number of input tessukuntadi
    ls.append(user_input)
print(ls)
user_input=int(input(" entr the city number"))
print(ls[user_input+1])


# In[ ]:


ls


# In[ ]:


test_case=int(input())
for i  in range (test_case):
    travelled_distance_by_chef=int(input(" enter the chef travelled distances from office to house : "))# from office to house
    total_distance_covered_by_chef_day=2*travelled_distance_by_chef
    total_distance_covered_by_chef_per_week=5*total_distance_covered_by_chef_day
    print(f'total_distance_covered_by_chef_per_week:-{total_distance_covered_by_chef_per_week}')


# In[ ]:


user_input=int(input())
temp=0
temp2=0
if user_input<=100:
    print("no charges")
elif user_input>100 and user_input<200:
    temp=user_input-100
    print(temp*5)
else:
    temp=100
    temp2=user_input-200
    print(temp*5+temp2*10)


# In[ ]:


test_case_size=int(input("test_case_size"))
for i in range(test_case_size):
    x,y=input().split()
    if int(x)>int(y):
        print(f"these is the best score in two attempts {x}")
    elif int(x)==int(y):
        print(f"both are same score no best score at here {x}")
    else:
        print(f"these is the best score in two attempts {y}")


# In[ ]:


lst=['heloo','hkhkj','gygiyiugiu','iuiu',"khgy","hhjhyjg","bkjkjj"]
for i in range(1,len(lst)):
    if i%2==1:
        print(lst[i])
    


# In[ ]:


for i in range(1,101):
    print(f'{i} is {i**3}')


# In[ ]:


user_input=float(input())
while user_input>0:
    print(bin(int(user_input)))
    break


# In[ ]:


i=1
temp=0
numbers_size=int(input("give the size of digits for finding average ('size')"))
while i<=numbers_size:
    user=int(input())
    temp+=user
    i+=1
print(temp/2)


# In[ ]:


i=0
temp=0
numbers_size=int(input("give the size of digits for finding average ('size')"))
while i<=numbers_size:
    user=input( " enter yhe digits in single line using space").split()
    temp+=int(user)
    i+=1
print(temp/2)


# In[ ]:


lst=["hello","apple","booty","cat",["dog","elephant","fan","kjds"],"gold","ice"]
for user_input in range (len(lst)):

    print(lst[user_input])
print("//////////")
print(lst[user_input][0])


# In[ ]:


lst=["hello","apple","booty","cat",["dog","elephant","fan","kjds"],"gold","ice"]
for j in range(len(lst)):
    #print(lst[j])
#number_elements_in_ls_lst=4
    for i in range(j):
        print(lst[j][i])


# In[ ]:


arr=["1",3,"hello","write"]
for i in range(len(arr)+3):
    arr[i+2:]=arr[i:]
print(arr)


# In[ ]:


lst=["hello","apple","booty","cat",["dog","elephant","fan","kjds"],"gold","ice"]
for ls in lst:
    for j in ls:
        print(j)


# In[ ]:


lst=["hello","apple","booty","cat",["dog","elephant","fan","kjds"],"gold","ice"]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j])


# In[ ]:


# Write a program to find if the given number is prime or not.
user_input=int(input())#3
count=0
if user_input==1:
    
    print("prime")
for i in range(1,user_input+1):#1,3
    if user_input%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("Not prime")


# In[ ]:


# Write a program to check if the given number is palindrome or not.
user_input=str(int(input()))
#temp=[user_input]
for i in range(0,len(user_input)//2):
    if user_input[i]==user_input[-(i+1)]:
        print("palindrome")
        break
    else:
        print("not")
        break


# In[ ]:


# Write a program to find the given number is positive or negative.
usr_input=int(input())
if usr_input==0:
    print("zero")
if usr_input<0:
    print("negative")
else:
    print("postive")
    


# In[ ]:


# Write a program to check if the given number is Armstrong or not.
user_input=str(int(input()))
lst=[]
temp=0
for i in range(len(user_input)):
    lst.append(int(user_input[i]))
for j in range(len(user_input)):
    temp+=lst[j]**3
if temp==int(user_input):
    print("amstron")
else:
    print("not")


# In[ ]:





# In[ ]:



    


# In[ ]:


n=3
us=str(153)
#for i in range(len(us)):
    
if int(us[0])**3+int(us[1])**3+int(us[2])**3==int(us):
    print("am")
else:
    print("jl")


# In[ ]:


# Write a program to check if the given strings are anagram or not
user_input_1=str(input())
user_input_2=str(input())
temp_1=[]
temp_2=[]
if len(user_input_1)==len(user_input_2):
    for i in range(len(user_input_1)):
        temp_1.append(user_input_1[i])
    for j in range(len(user_input_2)):
        temp_2.append(user_input_1[j])
    for k in range(len(user_input_1)):
        if temp_1[k:n] in temp_2:
            print("ANAGRAM")
            break
        else:
            print("NOT ANAGRAM")
            break
else:
    print("PLEASE ENTER SAME NUMBER OF STRINGS TO BOTH INPUTS")
    


# In[ ]:


# Write a program to find a factorial of a number.
user_input=int(input())
temp=1
for i in range(1,user_input+1):
    temp*=i
print(temp)
#     for j in range(i+1,user_input+1):
#         pass
    
#     print(i*j,end=" ")
    


# In[ ]:


# Write a program to find a fibonacci of a number.
user_input=int(input())
if user_input<=2:
    print("1")
else:
    print((user_input-1)+(user_input-2))


# In[ ]:


#123456 7  8  9
#112358 13 21 34


# In[ ]:


def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
fib(4)
fib(6)
fib(7)
fib(9)
fib(11)
fib(20)


# In[ ]:


# Write a program to find GCD of two numbers.


# In[ ]:


# Write a program to find a maximum of three numbers.
user_input=input().split()
if len(user_input)==3:
    
    if user_input[0]>user_input[1] and user_input[0]>user_input[2]:
        print(f'{user_input[0]} is heighest element in given input')
    elif user_input[1]>user_input[0] and user_input[1]>user_input[2]:
        print(f'{user_input[1]} is heighest element in given input')
    elif user_input[2]>user_input[1] and user_input[2]>user_input[0]:
        print(f'{user_input[2]} is heighest element in given input')
    else:
        

        if user_input[0]==user_input[1] and user_input[0]>user_input[2]:
            print(f'{user_input[0]} is heighest element in given input')
        elif user_input[1]==user_input[2] and user_input[1]>user_input[0]:
            print(f'{user_input[1]} is heighest element in given input')
        elif user_input[2]==user_input[0] and user_input[2]>user_input[1]:
            print(f'{user_input[2]} is heighest element in given input')
        else:
            print(f'{user_input[2]} is heighest element in given input because all input are same')
else:
    print("enter 3 numbers as input using space")


# In[ ]:


# Write a program to find a minimum of two numbers
user_input=input().split()
if len(user_input)==2:
    print(min(user_input))
else:
    print("enter 2 numbers as input using space")


# In[ ]:


# Write a program to find a maximum of two numbers
user_input=input().split()
if len(user_input)==2:
    print(max(user_input))
else:
    print("enter 2 numbers as input using space")


# In[ ]:


def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')


# In[ ]:


for i in range(5):
    for j in range(i+1):
        print(j*'*',end=" ")
    print()


# In[ ]:


for i in range(5):
    for j in range(i+1,5):
        print(j*'*',end=" ")
    print()


# In[ ]:


for i in range(1,5):
    print(i*' *')


# In[ ]:


for i in range(5,0,-1):
    print(i*'*')
for j in range(i+1):
    print(j*'$')


# In[ ]:


def myfunc(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 5
myfunc(n)


# In[ ]:


for i in range(1,6):
    for j in range(i):
        print(j,end=' ')
    print()


# In[ ]:


for i in range(1,6):
    for j in range(i):
        print(j,end=' ')
    print()


# In[ ]:


for n in range(2,9):
    for j in range(1,n):
        print(j)
    print()


# In[ ]:


for a in range(2,7):
    for b in range(1,a):
        print(a,b)
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# In[ ]:


for l in range(1,7):
    for j in range(1,l+1):
        print(j,end=" ")
    print()
    


# In[ ]:


for i in range(12):
    print(i)


# 1
# 2 3
# 4 5 6
# 7 8 9 10

# In[ ]:


for i in range(1,11):
    for j in range(1):
        print(i*j,end=" ")
print()


# In[ ]:


for i in range(1,5):
    for j in range():
        print(j,end=" ")
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# A
# B C
# D E F
# G H I J
# K L M N O

# In[ ]:





# In[ ]:





# In[ ]:



rows=5
alp=ord('A')
for i in range(rows):
    for j in range(i+1):
        print(chr(alp),end=' ')
        alp+=1
    print()
        


# In[ ]:


alph=ord('A')
for i in range(5):
    print(' '*(5-i-1),end=" ")
    for j in range(i+1):
        print(chr(alph),end=' ')
        alph+=1
    print()
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# Write a Python program that defines a function to calculate the factorial of a given number. Use this function to prompt the user for a number and print its factorial.Strings Assignment:
def solve(n):
    temp=1
    if n==0 or n==1:
        return 1
    else:
        solve(n)*solve(n-1)
  # for i in range(n,1,-1):
  #   temp*=i
    return temp
solve(5)
#here 
  
    
    


# In[ ]:


get_ipython().system('pip install tensorflow')


# In[ ]:


import tensorflow as tf


# In[23]:


def main():
    usr=get_input()
    price=items(usr)
def user_input():
    while True:
        try:
            if usr!=input().title():
                raise EOFError    
        except EOFError:
            break
    return usr
def items(usr):
    count=0
    items={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    if usr in items:
        count+=items.get(usr)
        print(f"Total:${count}")
    return count
main()


# In[123]:


class Node:
    def __init__(self,head):
        self.head=head
        print(self)
        self.next=None
    def traversal(self):
        self.curr=self
        

        


# In[124]:


obj=Node(1)
obj1=Node(2)
obj2=Node(3)


# In[125]:


obj


# In[126]:


obj.head


# In[133]:



print(obj.next)


# In[128]:


obj1.head


# In[129]:


obj1.next


# In[130]:


obj2.head


# In[131]:


obj2.next


# In[132]:


obj.traversal()


# In[218]:


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    


# In[225]:


class Linkedlist:
    def __init__(self):
        self.head=None
        self.count=0
    def __len__(self):
        return self.count
    def insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.count+=1
    def print_pat(self):
        tem=''
        curr=self.head
        while curr!=None:
            tem+=str(curr.value)+'->'
            curr=curr.next
        return tem[:-2]
        
        
        
    


# In[226]:


l=Linkedlist()


# In[227]:


l


# In[228]:


l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)


# In[229]:


l.count


# In[230]:


l.print_pat()


# In[ ]:





# In[ ]:





# In[ ]:




