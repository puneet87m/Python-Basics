#!/usr/bin/python3
import datetime
now = datetime.datetime.now()
name = input("Enter your name: ")
age = input("Enter you age: ")
year = now.year
born = year - int(age)
if born + 100 < year:
    print("You turned 100 in year", born + 100,". Many more to go")
elif born + 100 == year:
    print("Congratulations!!! for turning 100 in current year", born + 100, ". 100 more to go") 
else:
    print("Hi", name, "You will be 100 years old in", born + 100, ". Live healthy")
