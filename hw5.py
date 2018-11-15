#JLouzada
#This script prints out celsius from 0-20 and converts it to farenheit

startingRange = int(input("Please input starting range"))
endingRange = int (input"Please input ending range"))


print("Celcius Fahrenheit\n------------------")

for x in range(0,21,1):
    far = round(x * 9/5 + 32)
    print(x, "\t", far)
    print(" ")
