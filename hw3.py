#This script converts user input for celcius and fahrenheit degrees
#Jlouzada IT 116 MWF 1-1:50

#Collect user input for fahrenheit
fDegreeInput = int(input("Please enter the tempature in Fahrenheit: "))
#Tell user what they have inputted
print("You entered",fDegreeInput,"degrees Fahrenheit")
#Convert fahrenheit to celcius
fConversion = (fDegreeInput - 32) * 5/9
#Tell user what the conversion is for fahrenheit to celcius
print(fDegreeInput,"degrees Fahrenheit is",int(fConversion),"degrees Celcius")
print()
#Ask user for celcius input
cDegreeInput = int(input("Please enter the tempature in celcius: "))
#Tell user what they have inputted for celcius
print("You entered",cDegreeInput,"degrees celcius")
#Convert celcius to fahrenheit
cConversion = cDegreeInput* 9/5 + 32
#Tell user what the answer is
print(cDegreeInput,"degrees celcius is",int(cConversion),"degrees farenheit")

