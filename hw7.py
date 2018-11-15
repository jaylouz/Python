#Jlouzada. This script takes input for degree and converts it respectively

#This function converts celcius value to fahrenheit
def celcius_to_fahrenheit(celsius):
    celToFahr = round(celsius * 9/5 + 32)
    return celToFahr

#This function convers fahrenheit value to celsius
def fahrenheit_to_celsius(fahrenheit):
    subtraction = fahrenheit - 32
    fahrToCel= round(subtraction * 5/9)
    return fahrToCel

#This function prints out a table with min and max input as starting
#and ending range
def print_celsius_to_fahrenheit_conversion_table(min, max):
    print("Celcius \t", "Farhenheit\n-------------------------")
    for x in range(min,max+1):
        print(x, "\t", celcius_to_fahrenheit(x))
        print(" ")

#This function prints out a table with min and max input as starting
#and ending range
def print_fahrenheit_to_celsius_conversion_table(min, max):
    print("Fahrenheit \t", "Celsius\n-------------------------")
    for x in range(min,max+1):
        print(x, "\t", fahrenheit_to_celsius(x))
        print(" ")

#User prompts and executions
min_celsius = int(input("Enter minimum celsius tempature: "))
max_celsius = int(input("Enter maximum celsius temature: "))
print()
print_celsius_to_fahrenheit_conversion_table(min_celsius, max_celsius)
min_fahrenheit = int(input("Enter minimum Fahrenheit temperature: "))
max_fahrenheit = int(input("Enter maximum Fahrenheit temperature: "))
print()
print_fahrenheit_to_celsius_conversion_table(min_fahrenheit, max_fahrenheit)


