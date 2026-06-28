#PYTHON - BROCODE
#1.Basics
print("I like Pizza")   #Used to print anything
#Commnets - used by writing after '#'
#Pyhton is high leveled intendation(spacing) based language
#no need of ; as in c++

#2.Varibales - Datatypes: ( integer(int), float(float), boolean(bool), string(str) )
variable = "Bro"
vrr="""Triple quotes are used to write very long strings"""
print(f"Variable is {variable}")   #Use f to print variables too using {} 
var = True  #True and False ka T and F capital rakhna in boolean
#We can add or subtract two variables of same datatypes only

#3. Typecasting - There are rules like str can't be converted into int
num=3.2
print(type(num))   #Prints the datatype of that variable like <class 'float'>
new_num=int(num)   #Converts value of float into integer and stores in new_num

#4. User input 
age = int(input("What is your age"))    #input is by default str so we have to convert in desired datatype
#User have to click enter after giving an input to go in next step

#5. Game Project 

#6. arithmetic and operators - same in js(like exponents etc)
# +, -, *, /, **, +=, -=, *=, /=, %, ,=, ==, pow(x,y), max(x,y,z), min(x,y,z)
import math
print(max(4,5))
print(math.pi) 
print(math.e)
print(math.sqrt(4))     #ans = 2
print(math.ceil(4.2))   #ans = 5
print(math.floor(4.9))  #ans = 4
print(round(age,2))     #round off to 2 digits after decimal

#7. if statements
age=23
if age>=18:             #We can put booleans in place of conditons
    print("Adult\n")
elif age<=0:            #There can be infinite elifs allowed
    print("Invalid\n")
else:
    print("Child\n")

#8. Calculator program
#9. Weight conversion
#10. Temperature conversion F°=((9/5)*C°)+32    (Alt + 0176) = °

#11. logical operators - or, and, not
age>=18 and age<=100
age>=1 or age<=-1
age = not var   #Here var is a boolean type
#Bit wise operators never used for conditions
print(4 & 5)  #Gives binary and number

#12. Conditional expressions - Ternary operator
a=5
b=4
print(a if a>b else b)

#13. String Methods
name = "Bro Code"
re=len(name)        #gives length
re=name.find(" ")   #gives index of first occurence of character #Gives -1 if not exist
re=name.rfind("o")  #gives last occurence 
re=name.capitalize()    #Capitaize the first letter
re=name.upper()         #all uppercase
re=name.lower()         #all lowercase
re=name.isdigit()       #gives true if only contains digits #very imp
re=name.isalpha()       #gives true if all only contains alphabets
re=name.count("-")      #counts number of occurences of - in that string
re=name.replace("-"," ")    #replace all "-" with " "
print(help(str))        #It will show methods of str
print(re,end="OK")      #Har ek re ke baad mein OK likhega and new line mein each element nhi jayega
print("1","2","3",sep="-")  #All strings are seperated by - 

#14. String indexing
name = "Atharva"
#By indexing
print(name[0])   #Indexing starts at 0
print(name[0:4]) #Starting with indexing 0 and ending by including 3 and excluding 4th index
print(name[0:4:2])  #starts at 0 upto 3 and excluding 4 with steps of 2 --> A
print(name[1:])     #1 and baad ke sabhi print ho jayenge
print(name[:3])     #Excluding 3 tk shuru se sabhi print ho jayenge
print(name[-1])     #-1 represents the last character of string (Negative indexing starts from end)
print(name[-4:])    #Prints only last 4 characters

#15. format specifiers = {value:flags} format a value based on what flags are inserted
rev = 3.123456
print(f"{rev:.2f}") #.2f shows only 2 numbers are allowed after decimal
print(f"{rev:10}")  #Variable will occupy 10 spaces
print(f"{rev:<10}") #Variable will occupy less than 10 spaces accordinly
print(f"{rev:+}")   #Positive ke samne + aayega and negative ke samne -\
print(f"{rev:,}")   #Numbers mein comma layega 30,000
print(f"{rev:02}")  #Har number 2 digit ka hoga and 1 digits ke samne 0 lagega

#16. While loop
while name=="":     #Runs according to condition
    print("You not entered name")
    name=input("Enter your name")

#17. Compound interest calculator   amount=principal*pow((1+(r/100)),t)

#18. for loop
for x in range(1,11):   #11 is excluded and each number is printed new line
    print(x)

for x in reversed(range(1,11)): #reverse order mein print hoga 10,9,..1 in new line
    print(x)

for x in range(1,11,2): #1 3 5.. starts at 1 with gap of 2 upto 10 excluding 11
    print(x)

s="Atharva"
for x in s:             #Iterate through each character of string
    print(x)    

for x in range(1,21):
    if(x==13):
        continue    #skips iteration 
    if(x==19):
        break       #stops loop

#19. Coutdown timer program
#Time function
import time

for x in range(20,0,-1):    #20 se 1 tk ek-ek decrease order mein print hoga
    time.sleep(2)       #Iske baad ki process 2 sec rukne ke baad hi hogi
    print(f"Times going {x}")
    print(x,end=" ")   #Python by default print ke endl deta hai but end="" se same hi line mein rahoge and end="Ok" se her iteration ke baad Ok likh kr aayega and still in same line

#Project - second se hour minute and second mein time deta hai
mt=int(input("Enter seconds"))
for x in range(mt,0,-1):
    sec=x%60
    min=int(x/60)%60
    hour=int(x/3600)%60
    print(f"{hour}:{min}:{sec}")
    time.sleep(1)

#20. Nested loop - loop ke ander loop - patterns of DSA
for row in range(4):
    for col in range(4):
        print("*",end="")
    print()                 #To enter newline after consecutive ****

#21. Collections = single variable used to store multiple values
#List = [] ordered(indexed) and changable. Duplicates allowed #Mostly used
fruits=["apple","banana","apple","coconut"]    #Array
print(fruits)       #Prints the whole tuple
print(fruits[0])    #Iterate same as array
print(fruits[0:3])  #0 1 2 elements excluding at index 3
print(fruits[::2])  #elemets at index which are divisible by 2
print(fruits[::-1]) #prints all elements in reverse
print(dir(fruits))  #Shows all attributes applicable to this collection type
print(help(fruits)) #Shows all attributes along with their description of how they will work
print(len(fruits))
print("apple" in fruits)    #Prints True if apple is present in fruits
fruits.append("orange")
fruits.remove("banana")
fruits.insert(0,"pineapple")    #At 0th index pineapple is printed
fruits.sort()                   #sorts alphabetically
fruits.reverse()                #Jis order mein hai uske ulte order mein print hoga
fruits.index("apple")           #Jitne bhi index honge unme se firts occurance print hoga
fruits.count("apple")           #No. of times apple aaya usko count krega

#Set = {} unordered(indexing nhi hongi) and immutable, but add/remove allowed. Duplicates not allowed
fruits={"apple","banana","coconut","apple"} #Ek se jyada baar likh skte hai but print store ek hi baar hoga
print(fruits)
fruits.add("orange")
fruits.remove("apple")
fruits.pop()    #As set is unordered so uske hisab se jo element first pe honga vo remove ho jayega
fruits.clear()  #All elements are cleared
print(len(fruits))

#Tuple = () ordered and unchangable. Duplicates are allowed. FASTER #Cannot be added removed or changed
fruits = ("apple","orange","banana")
print(fruits.index("apple"))        #Other same methods just as lists
print(fruits.count("orange"))

#22. Shopping cart program

#23. 2D collections like excel spreadsheet
fruits=["apple","banana","orange"]
veg=["carrot","onion","tomato"]
groc=[fruits,veg]
print(groc[0][1])   #fruits me ka element at index 1 dega

#24. Quiz game

#25. Dictionaries = a collection of {key:value} pairs, ordered and changable. No duplicates
capital={"USA":"WDC","India":"Delhi","China":"Bejing"}
print(capital.get("India")) #Value associated with it is printed
capital.update({"Germany":"Berlin"})    #New key:value is added  #As using sets so ( { } ) use krna
capital.update({"USA":"Texas"})         #New value is assigned to existing key
capital.pop("USA")  #USA ki key select krne se wo pura remove ho jayega
capital.popitem()   #removes recently added key
capital.clear()     #Removes all key from dictionary
print(capital.keys())   #Prints all the keys present in dictionary

for key,value in capital.items():       #Way to print dictionary
    print(f"{key}:{value}")     

#26. Concession stand program

#27. Random numbers
import random
n1=random.random()     #Gives a random decimal number between 0 and 1

#28. Number guessing game
num=random.randint(1,6)
print(num)              #prints an integer between 1 and 6

#29. Rock,paper,scissor
options=("rock","paper","scissor")
select=random.choice(options)      #Gives random option among all options

#30. Dice Roller Program
cards=["1","2","3","4","5"]
random.shuffle(cards)               #Used to shuffle values in list

#31. Functions - place () after function name to invoke it  #Def means to define a function
def happy_birthday(name,age):           #Order of parameters matter
    print(f"Happy Birthday to {name} of age {age}")     

happy_birthday()    #This is function calling

def add(x,y):
    z=x+y
    return z

result=add(2,3)

# Types of Arguements:    1.DEFAULT    2.keywords   3.positional    4.arbitrary

#32. default arguements - A default value for certain parameters
#                         default is used when that arguement is omitted make you function more flexible, reduces # of arguements
def price(l,d=0,t=0.05):    #default arguements should be after positional arguements
    return l*(1-d)*(1+t)

price(500)  #As value of other parameters are not entered, they are set by default 

#33. Keyword arguements - an arguement preceded by an identifier helps with readability

def hello(g,t,f,l):
    print(f"{g}{t}{f}{l}")

hello("Hello",t="Mr",f="Vedant",l="Patil")    #positional arguements come before keyword arguements
#Jo arguements normally(according to position) kaam krte hai unhe positional arguements kehte hai

#34. args & **kwargs (Arbitrary arguements)                                 
# *args - By using arbitrary arguements it packs any number of parameters in 'tuple'
def add(*args):     
    print(args)     #Gives tuple datatype    
    sum=0
    for elem in args:
        sum+=elem
    return sum

print(add(3,4,5))  

#**kwargs - For storing key value pairs using keyword arguements
def func(**kwargs):                 
    print(type(kwargs))             #Gives dictionary datatype
    for value in kwargs.values():    #Gives all the values 
        print(value)
    
    for key in kwargs.keys():
        print(key)                  #Gives all the keys

    for key,value in kwargs.items():   
        print(f"{key}:{value}")     #Gives all key value pairs passed in functions

    print(f"{kwargs.get('a')}")     #Gives value associated with it

    if "b" in kwargs:               #Checks if b parameter is present in function or not  #membership operator
        print(f"{kwargs.get('b')}")

func(a=1,b=2,c=3) 

def fc(*args,**kwargs):     #args are declared before kwargs
    pass            #Here pass is used to temporarily run a function

#35. Iterable = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
# Tuple,strings are iterable and reversable but set cannot be reveresed however it is printable by iteration
# Dictionary - printing by loops example is shoen above by using .items()

#36. membership operators = used to test whether a value or variable is found in a sequence
#                            (string, list, tuple, set, or dictionary) 1.in  2.not in
email="Atharva1234@gmail.com"

if "@" in email and "." in email:
    print("E-mail accepted")

#37. List comprehensions = A concise way to create lists in Python
#                          Compact and easier to read than traditional loops [expression for value in iterable if condition]

list1 = []
for x in range(1,11):
    list1.append(x*2)

#Another way to do using formula [expression for value in iterable if condition]
list1=[]
list1=[x*2 for x in range(1,11)]    #Loop ka kaam krega #Comprehensions

fruits=["apple", "banana", "orange"]
fchars = [elem[0] for elem in fruits] #Prints the first character of every element in list

num=[1,-2,3,-4]
new_num=[x for x in num if x>0] #This time using complete formula having condition

#38. match-case statements (switch): 
day =1
match day:
    case 1 | 0: print("1") # | is used as or operator
    case 2: print("2")
    case _: print("Not valid")  #_ is run if no matching cases

#39. modules = file containing code wanna include in our program
print(help("modules"))  #Gives all the available modules

import math as m    #Alias to use module name like math.pi as m.pi
from math import pi #Not used due to confusion in variable name
#import banda       #Here banda is another python file name imported in this python file but it is commented to reduce warning

#40. variable scope = where a variable is visible or accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Build-in

#41. if name == 'main'
# Python har file ko ek naam deta hai: __name__
# Agar tum file direct run karte ho → __name__ = "__main__"
# Agar tum file import karte ho → __name__ = file ka naam

# Current file = a.py
print("A file start")

def main():
    print("Main function chal raha hai")

if __name__ == "__main__":
    main()

# Current file - b.py
# import a  - Commented to avoid warning
#The content of file a is same as given above then if we run file b 
# ->"A file start" is printed but "Main function chal raha hai" is not because __name__ == "__main__" this condition is false as main file is not file a it is now imported file

#42. banking program

#43. Slot Machine(Gambling machine) - good game

#44. Encryption program ✨

#45. hangman game

#----------------------------------✅OOPS✅-------------------------------------------
#46. Python Object Oriented Programming
#Object: A "bundle" of related attributes (variables) and methods (functions) 
#Class: (blueprint) used to design the structure and layout of an object

#47. class variables - Shared among all instances of a class
#Defined outside the constructor , allow you to share data among all objects created from that class

class Car:       
    color="red"                             #Here color and num are class variables declared outside constructor function                       
    num=0
    def __init__ (self, model, year):       #__init__ = Used to help initialize constructor objects
        self.model = model
        self.year = year
        Car.num+=1                          #Jitni baar no. of constructors declare hoge utne bar +1 hoga
    
    def drive(self):
        print("You are driving car")

    def describe(self):                     #Instance methods - belong to a particular object
        print(f"{self.model},{self.year}")

car1 = Car("BMW",2025)
car2 = Car("Audi",2023)     
print(car1)                 #Memory address of car1 dega #As pure object ko directly print nhi kr skte
print(car1.model)           #. method is used to show values of attributes
print(car1.color)           #red dega
print(Car.num)              #Gives number of constructed objects to this class - 2

car1.drive() #Instance Method  #It will print the that message 
car1.describe()             #It will print all values in object, function hi aisa banaya hai

#48. Inheritance: Allows a class to inherit attributes and methods from another class helps with code reusability and extensibility
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True  #Jo value user se nhi mangi jayengi vo parameter mein nhi aayengi

    def eat(self):          #Class method
        print(f"{self.name} is eating")

class Dog(Animal):      #Dog is inheriting from animal
    pass

dog=Dog("Scooby")       #It will use of Dog and Animal both classes

#49. Multiple inheritance = inherit from more than one parent class C(A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent  C(B) <- B(A) <- A

class Pichi(Dog,Animal):    #It will have inheritance of more than one class
    pass

#50. super() = Function used in a child class to call methods from parent class (superclass)
# Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color):
        self.color = color

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)         #Gets all values according to super function

#51. Polymorphism = Greek word that means to "have many forms or faces" | Poly = Many   Morphe=Form
#                   2. "Duck Typing"= Object must have necessary attributes/methods
#1. Inheritance = It is same as inheritance, if a class is child of another parent class then that class can be considered of two forms one of parent form and another of child form

#52. Duck typing = If it looks like duck and quacks like duck then it must be a duck
#If a class1 have all qualities as class2 then it can be said that class2 is parent of class1

#53. Static method = A method that belong to a class rather than any object from that class (instance)

#Instance methods = They belong to indivisual objects created from class (ex above)
#Static methods = Best for utility functions that do not need access to class data
class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position = position

    @staticmethod       #Is @ ke ander hi Jo data class ka nhi oose use kro
    def is_valid(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
print(Employee.is_valid("Manager"))     #Manager is included so it gives true

#54. Class Methods = Allow operations related to the class itself
#                   Take(cls) as first parameter, which represents the class itself
class Student:
    tgpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.tgpa+=gpa

    def describe(self):
        print(f"{self.name}, {self.gpa}")

    @classmethod        #Is @ ke ander hi cls use kr skte hai
    def cg(cls):
        if cls.count==0:
            return 0
        else:
            return f"Total gpa of students is {cls.tgpa}"   

#55. Magic methods - Dunder methods (double underscore) __init__, __str__
# They are automatically called by many of Python's build-in operations.
# They allow developers to define or customize the behavior of objects.
class Books:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        print(f"{self.name}")

    def __eq__(self, other):
        return self.name == other.name      #If two books have same name however diff variable name they would be called as equal
    
    def __lt__(self,other):
        return self.name<self.name          #It compares lexicographically
    
    def __add__(self,other):
        return self.name + other.name       #It adds names of two books
    
    def __contains__(self,keyword):
        return keyword in self.name         #If a keyword is present in name it gives true
    
    def __getitem__(self,key):
        if key=="name":
            return self.name                #Gives value of keyword parameter (like in dictionary)


book1=Books("Wings of fire")
book2=Books("Wings of fire")
print(book1)                #Earlier it was giving address but now giving name of book due to __str__
print(book1==book2)         #This will print true due to __eq__ method
print(book1.name<book2.name)    #Compares two names
print(book1.name+book2.name)    #Adds two names
print("Wings" in book1)     #Wings is present in book1
print(book1["name"])        #Gives parameter's assigned value to key "name" of book1 

#56. @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: Add additional logic when read,write,delete attributes
# Gives you getter(read), setter(write), and deleter(delete) method
class Rectangle:
    def __init__(self,width):
        self._width = width     #If we declare a property starting with _ then it can be used out of class

    @property                   #Getter - Used to get value
    def w(self):
        return f"{self._width:.2f} cm"
    
    @w.setter                   #Setter - Used to edit that property if we got incorrect input
    def w(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width must be greater than zero")

    @w.deleter                  #Deleter - used to delete value
    def width(self):
        del self._width         #del is used to delete value


    
rectangle=Rectangle(3,4)    #Class declared
print(rectangle.w)          #poperty @ ki wajah se class_name.property as function use kr skte hai
print(rectangle._width)     #This will give raw value
del rectangle.w             #Deleter used to delete that value

#57. Decorator - A function that extends behaviour of another function w/o modifying base function
# Pass base function as an arguement to decorator

def add_sprinkles(func):        #Decorator function is used to add some special properties to selected functions
    def wrapper(*args,**kwargs):#args,kwargs is used to get values from original function
        print("Statement 1")
        func(*args,**kwargs)                  #We have to return the base function which we recieve 
    return wrapper              #Also return the additional changes we have made with original functions

@add_sprinkles              #This @ is used for decorator
def get_ice_cream():
    print("Statement 2")

get_ice_cream() #Both Statement 1 and Statement 2 are printed

#58. exception - An event that interrupts the flow of program (ZeroDivision, TypeError, ValueError)  1]try  2]except  3]finally
try:
    n=int(input("Enter number"))
    print(1/n)
except ZeroDivisionError:
    print("You can't divide by zero")   #Dividing by zero gives error so this executes
except ValueError:
    print("Enter only Numbers")
except Exception:
    print("error occurs due to some reason")    #It is bad practice because it does not specify error type
finally:
    print("Do some clean up")   #Finally block is executed always without any error or something

#59. file detection - 
import os   #Operating systems se interact krne ke liye
file_name = "test.txt"
if os.path.exists(file_name):       #If file/directory exists then this executes otherwise not
    print(f"The location {file_name} exists")

if os.path.isfile(file_name):       #If it is a file or not
    print(f"That is a file")

#60. writing files (.txt, .json, .csv)
#txt file
this_data="I like Dosa"
file_path = "C:/Users/HP/Desktop/file_name.txt"
try:
    with open(file=file_path, mode="w") as file1: #A new notepad file will be created and written accordingly
        file1.write(this_data)        #We cannot write whole tuples or lists
except FileExistsError:
    print("File already exists")
except PermissionError:
    print("You d0 not have permission")

#json file
import json
new_file="C:/Users/HP/Desktop/file_name.json"
employee={
    "name":"Abc",
    "age":20,
    "job":"cook"
}
with open(new_file,"w") as file2:
    json.dump(employee, file2)       #This is used to write json file

#csv file - they are just like excel spreadsheet
import csv
Data2d=[["Name","age","Job"],["HP",30,"Cook"],["Pat",27,"Scienist"]]
file_p2="C:/Users/HP/Desktop/file_name.csv"

with open(file_p2,"w",newline="") as file3:
    writer=csv.writer(file3)
    for row in Data2d:
            writer.writerow(row)    #It is used to write all list's rows like spreadsheet

#61. Reading files
#txt file
file_p2="C:/Users/HP/Desktop/file_name.csv"
with open(file_path,"r") as file4:
    content = file4.read()  #It is used to read a file
    print(content)          #This shows content in the file

#json file
file_p2="C:/Users/HP/Desktop/file_name.json"
with open(file_path,"r") as file5:
    content = json.load(file5)
    print(content)

#csv file
file_p2="C:/Users/HP/Desktop/file_name.csv"
with open(file_p2,"r") as file6:
    content=csv.reader(file6)
    for line in content:
        print(line)

#62. dates & times
import datetime
import time
import pygame                   #pip se install kr lena
v1=datetime.date(2025,1,2)    #Puts this in YYYY-MM-DD
v2=datetime.date.today()     #Todays date
v3=datetime.time()            #Current time
v4=datetime.datetime.now()     #Todays date and time
v5=v4.strftime("%H:%M:%S %m-%d-%y")      #Shows hour,minute,second,month,day,year

#Comparison of duration
target = datetime.datetime(2030,1,2,12,30,1)
curr = datetime.datetime.now()

if target<curr:
    print("Time hai bhai")
elif target==curr:
    print("Ho rha")
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()   
    while pygame.mixer.music.get_busy():
        time.sleep(1)           #Jb tk music khatam nhi tb tk program chalega
else:
    print("Ho gya")

#63. Python Alarm clock

#64. multithreading - Used to perform multiple tasks concurrently(multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs threading. Thread (target=my_function)

import threading
def task1(first):
    time.sleep(5)
    print(f"Done1 {first}")

def task2():
    time.sleep(2)
    print("Done2")  

#Earlier we have got task1 before task 2 
#By using threading fastest task will be exectued first order - task2 then task1
chore1=threading.Thread(target=task1,args=("Scooby",))  #Only tuple can be passed in args in mutithreading #Bich mein comma dena
chore1.start()
chore2=threading.Thread(target=task2)
chore2.start()

chore1.join()   #Isse kya hota hai - 
chore2.join()   

#65. Connecting to an API using Python
import requests
Our_url="https:/pokeapi.co/api/v2/"
def get_info(name):
    url = f"{Our_url}/pokemon/{name}"
    responce=requests.get(url)
    print(responce)             #It gives http  status code 200 means ok

    if responce.status_code==200:
        print("Responce is ok")
        print(responce.json())  #It gives json file of that api

name="pikachu"
pok_info=get_info(name)

if pok_info:
    print(f"{pok_info["id"]}")    #It selects value of the key passsed in it

#End

#pytest
this_data="I like Dosa"
file_path = "C:/Users/HP/Desktop/file_name.txt"
try:
    with open(file=file_path, mode="w") as file1: #A new notepad file will be created and written accordingly
        file1.write(this_data)
except PermissionError:
    print("You d0 not have permission")

import pytest
import sys
def test_calc_total():
    total = file1.calc_total(4,5)   #Before this make a file1 and write a function calc_total in it
    assert total == 9               #Use to verify if result is correct or not
#Do 'python -m pytest' - Write this in terminal
#This will go recursively among all files and look for files which have 'test_' prefix and execute all methods with 'test_' prefix
#assert shows testcase, and this command shows if is passed or failed
#Do 'py.test -v -rxs' This shows details of testcases along with reasons

@pytest.mark.skip(reason="I dont want to run this test")    #This will skip the testcase
def test_calc():
    total = file1.calc_total(4,5)   
    assert total == 9

@pytest.mark.skipif(sys.version_info>=(3,5))    #This is way to write 3.5 version  #Testcase will be skipped if version is greater than 3.5
def test_calc():
    total = file1.calc_total(4,5)   
    assert total == 9  

#pytest -k multiply -v : Check only those testcases which have multiply in their name

#We can also use @ to seperate them in category
@pytest.mark.category_1
def test_w_1():
    pass

@pytest.mark.category_1
def test_w_2():
    pass

@pytest.mark.category_2
def test_w_3():
    pass

#pytest -m category_1 -v : It will run only category_1 wali testcases
#pytest -m "not category_1" -v : It will run all testcases except category_1 wali

from fixtures import MyDB

conn = None
cur = None

def setup_module(module):   #Use to connect and setup mydb
    global conn
    global cur
    db=MyDB()   #Har baar MyDB() use krne se accha bas db use kro   #It is costly operation
    conn=db.connect("server")   #.connect is usd to connect Database to server
    cur=conn.cursor()           #.cursor is used to ???

def teardown_module(module):    #For cleanup tasks after everything is done
    cur.close()
    conn.close()

def test_John_id():
    id=cur.execute("select id from employee_db where name='John'") #.execute is use to do the sql task
    assert id==123

#This can be done in another short method
#To print the messages in fixture also do 'pytest -v --capture=no'
@pytest.fixture()
def cursor_1():
    print("setting up") #Prints message before verifying testcases
    db=MyDB()
    conn=db.connect("server")
    curs=conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing DB") #Prints message after verifying the testcases

def test_John_id(cursor_1):  #Just pass callbck of above function
    id=cur.execute("select id from employee_db where name='John'") 
    assert id==123

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5,25),
                             (9,81),
                             (10,100)
                         ]
                         )
def test_cal_square(test_input, expected_output):
    result = file1.cal_square(test_input)   #This gets input from parametrize's first value of each paired tuple
    assert result==expected_output