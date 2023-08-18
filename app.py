weight = float(input("What is your weight: "))
unit = input("Is this in (K)ilograms or (L)bs: ")
convertedWeight = 0

if unit.upper() == ("L"):
    convertedWeight = (weight / 2.20462)
    print("Your weight in Kilograms is: " + str(convertedWeight))
elif unit.upper() == ("K"):
    convertedWeight = (weight * 2.20462)
    print("Your weight in Lbs is: " + str(convertedWeight))