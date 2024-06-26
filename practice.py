# -*- coding: utf-8 -*-
"""practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15QZYdBUEUr7WvTXup42g0NguSrifHzwE
"""



"""## lambda function :-

"""

#in lambda function we can write the small code in a single line
list_ = [35, 12, 69, 55, 75, 14, 73]
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))
print('The list of odd number is:',odd_list)

numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
square_list = list(map(lambda num: num**2, numbers_list))
print('Square of the list is', square_list)

numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
square_list = list(map(lambda num: num**2, numbers_list))
print('Square of the list is', square_list)

Minimum = lambda x,y : x if (x<y) else y
print('The greater number is:', Minimum( 35, 74 ))

#sorting :-it sorts the elements in a-z or 0-9 means in ascending order
my_List = [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]
# sorting every sublist of the above list
sort_List = lambda num : ( sorted(n) for n in num )
# Getting the third largest number of the sublist
third_Largest = lambda num, func : [ l[ len(l) - 2] for l in func(num)]
result = third_Largest( my_List, sort_List)
print('The third largest number from every sub list is:', result )
print(sorted(my_List) )

"""## while and for loop"""

#whle loop :-With the while loop we can execute a set of statements as long as a condition is true.
i=1
while i<10:
    print(i)
    if i==3:
      break
    i=i+1

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=(" "))
    print()

"""## functions"""

#abs function converts negative to positive anf positive math.remainderinteger = -20
print('Absolute value of -40 is:', abs(integer))

k = [1, 3, 4, 6]
print(all(k))

x =  10
y =  bin(x)
print (y)

string = "Hello World."
array = bytes(string, 'utf-8')
print(array)
print(callable (string))

x= 8
print(callable(x))

x=8
exec('print(x==8)')
exec('print(x+8)')

print('Pyth\xf6n is interesting')

"""## file handling"""

a = ["Python", "Exceptions", "try and except"]
try:
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array
     for i in range( 4 ):
        print( "The index and element from the array is", i, a[i] )
#if an error occurs in the try block, then except block will be executed by the Python interpreter
except:
    print ("Index out of range")

def square_root( Number ):
    assert (( Number < 0),"Give a positive integer")
    return Number**(1/2)

#Calling function and passing the values
print( square_root( 36 ) )
print( square_root( -36 ) )

def reciprocal( num1 ):
    try:
        reci = 1 / num1
    except ZeroDivisionError:
        print( "We cannot divide by zero" )
    else:
        print ( reci )
# Calling the function and passing values
reciprocal( 4 )
reciprocal( 0 )

try:
    div = 4 // 1
    print( div )
# this block will handle the exception raised
except ZeroDivisionError:
    print( "Atepting to divide by zero" )
# this will always be executed no matter exception is raised or not
finally:
    print( 'This is code of finally clause' )

"""## date and time"""

import time;
#prints the number of ticks spent since 12 AM, 1st January 1970
print(time.time())

import time;

#returns a time tuple

print(time.localtime(time.time()))

"""## iterations"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a

      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

"""## class and object"""

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

class cars:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  def move(self):
    print('drive')


class boat:
  def __init__(self,brand,model):
    self.brand= brand
    self.model= model
  def move(self):
    print('ssail')

class plane:
  def __init__(self,brand,model):
    self.brand= brand
    self.model= model
  def move(self):
    print('fly')

car1=car('ford','mustang')

"""## date and time"""

import datetime
x= datetime.datetime.now()
print(x)

import datetime
x= datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2020,5,17)
print(x)

import datetime
x = datetime.datetime.now()
print(x)

x=datetime.datetime.now()
print(x.strftime("%C"))

"""## inbuilt math functions"""



x=pow(4,4)
print(x)

import math
x=math.sqrt(64)
print(x)

import math
x=math.ceil(1.4)
y=math.floor(1.4)
print(x)
print(y)

x=math.pi
print(x)

import json

"""## json"""



x='{"name":"john","age":21,"city":"newyork"}'
y=json.loads(x)
print(y["age"])

x={
  "name":"john",
  "age":21,
  "city":"newyork"
}
y=json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print("hello")

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  # def __str__(self):
  #   return f"{self.name}({self.age})"
  def myfunc(abc):
    print("hello my name is "+ abc.name)

p1=person("john", 20)
p1.myfunc()

p1.age=40

print(p1)

del p1.name

p1.myfunc()

class person:
  pass

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class

#super function:-Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class student(Person):
  def __init__(self,fname,lname,year):
    self.fname=fname
    self.lname=lname
    self.year=year
    super().__init__(fname,lname)
    self.year=year
  def welcome(self):
    print("welcome",self.firstname,self.lastname,"to the class of", self.year)
x=student("john","doe",2019)
# print(x.year)
print(x.welcome()

# iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"

for x in mystr:
  print(x)

class mynumbers:
  def  __iter__(self):
    self.a=1
    return self
  def __next__(self):
    if self.a<=20:
      x=self.a
      self.a+=1
      return x
    else:
      raise StopIteration

myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# here we used polymorphism which used when we have same operation in many class
class car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print('drive')
class boat:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print('sail')
class plane:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print('fly')

car1=car('ford','mustang')
boat1=boat('ibiza','touring 20')
plane1=plane('boeing','747')

for x in (car1,boat1,plane1):
  x.move()

"""##json file import  and  load,dump"""

# from pickle import dumps
import json

# Load the JSON file
file_path = '/content/sample.json'
with open(file_path, 'r') as file:
    data = json.load(file)
    # print(data)


# Parse and print the data using a loop
for country in data:
    print(f"Name: {country['name']}")
    print(f"Code: {country['code']}")
    print(f"Capital: {country['capital']}")
    print(f"Region: {country['region']}")
    print("Currency:")
    print(f"  Code: {country['currency']['code']}")
    print(f"  Name: {country['currency']['name']}")
    print(f"  Symbol: {country['currency']['symbol']}")
    print("Language:")
    print(f"  Code: {country['language']['code']}")
    print(f"  Name: {country['language']['name']}")
    print(f"Flag URL: {country['flag']}")
    print(f"Dialling Code: {country['dialling_code']}")
    print(f"ISO Code: {country['isoCode']}")
    print("="*40)

# python = json.dumps(data)
# print(python)

# locol scope :- when a variable created inside that function
# def myfunc():
#   x=300
#   print(x)
# myfunc()



# function inside a function
# def myfunc():
#   x=300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# myfunc()


# global scope :- when a variable created outside the function
# x=300
# def myfunc():
#   print(x)
# myfunc()
# print(x)


# globle keyword :-
# x=300
# def myfunc():
#   global x
#   x=200
# myfunc()
# print(x)


# non local:-

"""## practices for basics"""

#addition using different methods and function

#normal method
# num1=5
# num2=10
# print(num1+num2)

#normal method
# num1=5
# num=num1+num2
# print(num)

#using eval function
# num1 = eval(input("Enter a number: "))
# num2 = eval(input("Enter a number: "))
# print(num1+num2)

#using function
# def add(x,y):
#   return x+y

# num1 = eval(input("Enter a number: "))
# num2 = eval(input("Enter a number: "))
# num3=add(num1,num2)
# print(num3)

#using lambda function
# add_numbers = lambda x,y : x+y
# print(add_numbers(10,20))

#using recursive function to add two numbers
# def add(x,y):
#   if y==0:
#     return x
#   else:
#     return add(x+1,y-1)
# num1 = eval(input("Enter a number: "))
# num2 = eval(input("Enter a number: "))
# num3=add(num1,num2)
# print(num3)

x1=input()

2

#minimum of two no.s using function

# def minimum(a,b):
#   if a<b:
#     return a
#   else:
#     return b
# a = eval(input("Enter a number: "))
# b = eval(input("Enter a number: "))
# print(minimum(a,b))


# using min() function

# a = eval(input("Enter a number: "))
# b = eval(input("Enter a number: "))
# # print(min(a,b))
# minimum = min(a,b)
# print(minimum)

#using sorting method

# a=2
# b=3
# print(sorted([a,b])[0])


#using lambda function

# from functools import reduce
# a=2
# b=3
# minimum = reduce(lambda x,y:x if x<y else y,[a,b])
# print(minimum)



# maximum of two numbers
# a=2
# b=3
# print(max(a,b))

#using lambda function
# from functools import reduce
# a=2
# b=3
# maximum = reduce(lambda x,y:x if x>y else y,[a,b])
# print(maximum)

#using sorting function
# a=2
# b=3
# print(sorted([a,b])[-1])

# factorial of a number

# factorial using for loop
# num=eval(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#   fact=fact*i
# print(fact)

#factorial using function
# def factorial(n):
#   if (n==1 or n==0):
#     return 1
#   else:
#     return n*factorial(n-1)
# num = eval(input("Enter a number: "))
# print(factorial(num))

#factorail using function iterative approch
# def factorial(n):
#   if n<0:
#     return 0
#   elif (n==0 or n==1):
#     return 1
#   else:
#     fact = 1
#     while (n>1):
#       fact=fact*n
#       n=n-1
#     return fact
# n=eval(input("Enter a number: "))
# print(factorial(n))

# def factorial(n):
#   res=1
#   for i in range(1,n+1):
#     res*=i
#   return res

# n=eval(input("Enter a number: "))
# print(factorial(n))

#in math we have a predefined function for factorial
# import math
# n=eval(input("Enter a number: "))
# print(math.factorial(n))

# in numpy we have a inbuilt funtion numpy.prod() to find factorial
# import numpy as np
# n= eval(input("enter the number:"))
# print(np.prod([i for i in range(1,n+1)]))

# to find simple interest
# def simple_interest(p,t,r):
#   print('the principle is' ,p)
#   print('the time is' ,t)
#   print('the rate is' ,r)
#   si=(p*t*r)/100
#   print('the simple interest is' ,si)
#   return si
# p=eval(input('enter the principle:'))
# t=eval(input('enter the time:'))
# r=eval(input('enter the rate:'))
# simple_interest(p,t,r)

# simple_interest(1000,5,10)

#formula to find compound interest

# def compound_interest(principle,rate,time):
#   amount=principle*(1+(rate/100))**time
#   ci=amount-principle
#   print(ci)
# compound_interest(1000,5,7)

# p= 1200
# t=5
# r=10
# a=p*(1+(r/100))**t
# ci= a-p
# print(ci)

"""## code to check the given no. is armstrong or not

"""

# #armstrong number
# n = eval(input("Enter the number: "))
# sum = 0
# temp = n
# x=len(str(n))
# while temp > 0:
#     digit = temp % 10
#     sum +=digit**x
#     temp //= 10

# if sum == n:
#     print("The given number is an Armstrong number")
# else:
#     print("The given number is not an Armstrong number")

"""## to find the area of the given code

"""

# to find the area of the circle
# r=eval(input('enter the radius:'))
# area=3.142*r*r
# print(area)


#easy to write code if you know the formula



"""##arrays"""

# In below code Python create array : one of integers and one of doubles.It then prints the contents of each array to the console.

# import array as arr
# a=arr.array('i',[1,2,3,4,5])
# print("the new created is : ",end=' ')
# for i in a:
#   print(i,end=' ')


# Adding Elements to a Array
# import array as arr
# a=arr.array('i',[1,2,3])
# print("the new created is : ",end=' ')
# for i in a:
#   print(i,end=' ')
# print()
# a.insert(0,7)
# print("array after inserting : ",end=' ')
# for i in a:
#   print(i,end=' ')

#Accessing Elements from the Array(with the help of index no. we can access the array)
# import array as arr
# a=arr.array('i',[1,2,3,4,5,6,7,8,9])
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# print(a[8])


#Removing Elements from the Array
# import array as arr
# a=arr.array('b',[1,2,3,4,5,6,7,8,9])
# print(a)
# a.pop(1)
# print(a)
# a.remove(4)
# print(a)


#slicing the element of the array
# l=[1,2,3,4,5,6,7,8,9]
# print("array: ",end= ' ')
# for x in l:
#   print(x,end=' ')
# sliced_array=l[0:9:2]
# print('\n',sliced_array)

# searching in array(getting index number)
# print(l.index(1))

#updating the element in array(with the help of index no. we can update the array)
# l[0]=6
# print(l)


# different operations in array
# z=[1,3,2,5,3,4,7,8,5]
# print(z)
# z.sort()
# print(z)
# z.reverse()
# print(z)
# z.count(5)
# print(z)
# z.clear()
# print(z)


#to extend the array(with the help of for loop we can remove the list braket and print only no.s)
# v=[1,2,3,4,5]
# print(v)
# for i in v:
#   print(i,end=' ')
# print()
# v.extend([6,7,8])
# print(v)
# for i in v:
#   print(i,end=' ')

# to reverse the array
# l1=[22,3,3,22,55,22,55,22,88,65]
# l1.reverse()
# print(l1)


#to rotate the array
# def rotate_array(arr,max,no_of_element):
#   temp=[]
#   i=0
#   while (i<no_of_element):
#     temp.append(arr[i])
#     i+=1
#   while(no_of_element<max):
#     arr[i]=arr[no_of_element]
#     i+=1
#   arr[i]=temp
#   return arr

# arr=[1,2,3,4,5,6,7,8,9]
# rotate_array(arr,9,3)

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr=[1,2,3,4,5,6,7,8,9]
rotateArray(arr,9,2)

