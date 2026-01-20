voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

current = voltage / resistance
print("Current:", current)

if current < 0.5:
    print("Low current")
elif 0.5 <= current <= 2:
    print("Normal current")
else:
    print("High current")