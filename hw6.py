#JLouzada
#This script takes user input for beginning and ending range of temp they want and converts it into celcius and farenheit

def print_conversion_table(startingRange, endingRange):
    print("Celcius | Fahrenheit\n------------------")
    for x in range(startingRange,endingRange,1):
        far = round(x * 9/5 + 32)
        print(x, "\t", far)
        print(" ")

startingRange = int(input("Please input starting range: "))
endingRange = int (input("Please input ending range: "))
print(" ")
print_conversion_table(startingRange, endingRange)
