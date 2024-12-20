#Conditions

#Example1:

a=5
b=5
if a==b:
    print(True)
    
#Example2:

age = 21
if age>18:
    print("You can vote")
    
else:
    print("You are not eligible")

#Example3:

a=5
b=10
if a==b:
    print(True)
    
else:
    print(False)

#Example4:

age = 16
if age>18:
    print("You can vote")
    
else:
    print("You are not eligible")

#Example5:

#leap year or not
year = int(input("Enter a year: "))
if (year%4 == 0):
    print("Year is a leap year")

else:
    print("Year is not a leap year")

#elif statement Example6:

#Selecting the appropriate gear based on speed
input_speed = 1200

if input_speed>1000:
    print("Select gear 1")

elif 1000<input_speed<= 2000:
    print("Select gear 2")

else:
    print("Select gear 3")

age = 65
if age<10:
    print("You are a minor")

else:
    if age<60:
        print("You are an adult")
    else:
        print("You are a senoir")
        


    
    
