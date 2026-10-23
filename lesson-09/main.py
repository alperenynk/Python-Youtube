# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ").upper()

if unit == "K":
    weight = weight * 2.20462
    print(f"Your weight in pounds is: {weight:.2f} lbs")
elif unit == "L":
    weight = weight / 2.20462
    print(f"Your weight in kilograms is: {weight:.2f} kg")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

