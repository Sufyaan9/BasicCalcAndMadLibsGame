from math import *

## Basic Calculator

print("Basic Calculator")
print("")

num1 = input("Choose a number: ")
num2 = input("Choose another number: ")

## num1 & num2 are initially string values from input(). Convert them into either int() or float() for correct result
result = float(num1) + float(num2)
resultCeil = ceil(result)
resultFloor = floor(result)
resultMax = max(num1, num2)
resultMin = min(num1, num2)

## Numbers MUST be converted into string values using str() in print() to output with other string values
print("Addition: " + str(result) + "\n" + "Ceil result: " + str(resultCeil) + "\n" + "Floor result: " + str(resultFloor))
print("Maximum value: " + str(resultMax) + "\n" + "Minimum value: " + str(resultMin))

print("_________________________________________________________")
print("")

## Mad Libs Game

print("Mad Libs Game")
print("")

pet = input("Choose a pet: ")
colour = input("Choose a colour: ")
age = input("Choose an age: ")

## Convert var 'age' to a float within the string conversion str().
print("My pet is a " + pet + "\n" + "He is the colour " + colour + "\n" + "He is " + str(float(age)) + " years old")
